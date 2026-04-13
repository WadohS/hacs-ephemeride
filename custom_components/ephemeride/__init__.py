"""Ephemeride integration for Home Assistant."""
from __future__ import annotations

import logging
from datetime import timedelta
import json
import os

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.util import dt as dt_util

from .const import CONF_LANGUAGE, DOMAIN
from .data import build_day_payload
from .liturgical import get_movable_liturgical_days

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ephemeride from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    coordinator = EphemerideDataUpdateCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = {
        "coordinator": coordinator,
        "update_listener": entry.add_update_listener(async_update_options),
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        entry_data = hass.data[DOMAIN].pop(entry.entry_id)
        entry_data["update_listener"]()

    return unload_ok


async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload the entry when options are updated."""
    await hass.config_entries.async_reload(entry.entry_id)


def get_entry_language(entry: ConfigEntry) -> str:
    """Return the configured language, preferring options over initial data."""
    return entry.options.get(CONF_LANGUAGE, entry.data.get(CONF_LANGUAGE, "fr"))


class EphemerideDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Ephemeride data."""
    
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        self.entry = entry
        self.language = get_entry_language(entry)

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(hours=1),
        )

    async def _async_update_data(self):
        """Fetch data from Ephemeride."""
        try:
            # Use hass.async_add_executor_job for blocking I/O
            file_path = os.path.join(
                os.path.dirname(__file__),
                "languages",
                f"{self.language}.json"
            )

            # Read file in executor to avoid blocking
            data = await self.hass.async_add_executor_job(
                self._read_json_file, file_path
            )

            now = dt_util.now()
            tomorrow_date = now + timedelta(days=1)
            today = now.strftime("%m-%d")
            tomorrow = tomorrow_date.strftime("%m-%d")
            movable_days_today = get_movable_liturgical_days(now.year, self.language)
            movable_days_tomorrow = get_movable_liturgical_days(tomorrow_date.year, self.language)

            today_saints_raw = self._merge_entries(data.get(today, []), movable_days_today.get(today, []))
            tomorrow_saints_raw = self._merge_entries(data.get(tomorrow, []), movable_days_tomorrow.get(tomorrow, []))

            today_payload = build_day_payload(today_saints_raw, self.language)
            tomorrow_payload = build_day_payload(tomorrow_saints_raw, self.language)

            return {
                "saint_aujourdhui": today_payload["first"],
                "saint_demain": tomorrow_payload["first"],
                "type_aujourdhui": today_payload["first_type"],
                "type_demain": tomorrow_payload["first_type"],
                "tous_saints_aujourdhui": today_payload["names"],
                "tous_saints_demain": tomorrow_payload["names"],
                "nombre_saints_aujourdhui": today_payload["count"],
                "nombre_saints_demain": tomorrow_payload["count"],
                "details_aujourdhui": today_payload,
                "details_demain": tomorrow_payload,
                "langue": self.language,
                "date": now.strftime("%Y-%m-%d"),
            }

        except FileNotFoundError:
            _LOGGER.error("Fichier de langue non trouve: %s", file_path)
            raise UpdateFailed(f"Fichier de langue non trouve: {self.language}")
        except json.JSONDecodeError as err:
            _LOGGER.error("Erreur lors du decodage JSON: %s", err)
            raise UpdateFailed(f"Erreur JSON: {err}")
        except Exception as err:
            _LOGGER.error("Erreur inattendue: %s", err)
            raise UpdateFailed(f"Erreur: {err}")

    def _read_json_file(self, file_path: str) -> dict:
        """Read JSON file (blocking operation run in executor)."""
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _merge_entries(self, base_entries: list[object], extra_entries: list[object]) -> list[object]:
        """Merge fixed and movable entries while avoiding duplicates."""
        merged = list(base_entries)
        seen = {json.dumps(entry, ensure_ascii=False, sort_keys=True) for entry in merged}
        for entry in extra_entries:
            entry_key = json.dumps(entry, ensure_ascii=False, sort_keys=True)
            if entry_key not in seen:
                merged.append(entry)
                seen.add(entry_key)
        return merged
