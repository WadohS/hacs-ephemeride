"""Ephemeride integration for Home Assistant."""
from __future__ import annotations

import logging
from datetime import datetime, timedelta
import json
import os

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, CONF_LANGUAGE

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ephemeride from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    coordinator = EphemerideDataUpdateCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok


class EphemerideDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Ephemeride data."""
    
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        self.entry = entry
        self.language = entry.data[CONF_LANGUAGE]
        
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
            
            today = datetime.now().strftime("%m-%d")
            tomorrow = (datetime.now() + timedelta(days=1)).strftime("%m-%d")
            
            today_saints = data.get(today, [])
            tomorrow_saints = data.get(tomorrow, [])
            
            # Limit to 5 saints in attributes to avoid exceeding 16KB limit
            MAX_SAINTS = 5
            
            return {
                "saint_aujourdhui": today_saints[0][0] if today_saints else "Inconnu",
                "saint_demain": tomorrow_saints[0][0] if tomorrow_saints else "Inconnu",
                "tous_saints_aujourdhui": [s[0] for s in today_saints[:MAX_SAINTS]],
                "tous_saints_demain": [s[0] for s in tomorrow_saints[:MAX_SAINTS]],
                "nombre_saints_aujourdhui": len(today_saints),
                "nombre_saints_demain": len(tomorrow_saints),
                "langue": self.language,
                "date": datetime.now().strftime("%Y-%m-%d"),
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
