"""Capteurs pour l'integration Ephemeride."""
from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator

from .const import (
    CATEGORY_AUTRE,
    CATEGORY_DATE_RELIGIEUSE,
    CATEGORY_FETE,
    CATEGORY_SAINT,
    CATEGORY_SAINTE,
    CONF_LANGUAGE,
    DOMAIN,
    ENTITY_TITLES,
    INTEGRATION_VERSION,
    SENSOR_AUTRE_NAME,
    SENSOR_DATE_RELIGIEUSE_NAME,
    SENSOR_FETE_NAME,
    SENSOR_NAME,
    SENSOR_SAINT_MASCULIN_NAME,
    SENSOR_SAINTE_NAME,
    UNKNOWN_STATE,
)

_LOGGER = logging.getLogger(__name__)

SENSOR_DEFINITIONS = [
    {"key": "general", "unique": SENSOR_NAME, "category": None},
    {"key": CATEGORY_SAINT, "unique": SENSOR_SAINT_MASCULIN_NAME, "category": CATEGORY_SAINT},
    {"key": CATEGORY_SAINTE, "unique": SENSOR_SAINTE_NAME, "category": CATEGORY_SAINTE},
    {"key": CATEGORY_FETE, "unique": SENSOR_FETE_NAME, "category": CATEGORY_FETE},
    {
        "key": CATEGORY_DATE_RELIGIEUSE,
        "unique": SENSOR_DATE_RELIGIEUSE_NAME,
        "category": CATEGORY_DATE_RELIGIEUSE,
    },
    {"key": CATEGORY_AUTRE, "unique": SENSOR_AUTRE_NAME, "category": CATEGORY_AUTRE},
]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Configurer les capteurs a partir d'une entree de configuration."""
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    lang = entry.options.get(CONF_LANGUAGE, entry.data.get(CONF_LANGUAGE, "fr"))

    entities = [
        EphemerideSensor(coordinator, entry, lang, definition["category"], definition["unique"], definition["key"])
        for definition in SENSOR_DEFINITIONS
    ]
    async_add_entities(entities)


class EphemerideSensor(CoordinatorEntity, SensorEntity):
    """Representation d'un capteur Ephemeride."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        entry: ConfigEntry,
        lang: str,
        category: str | None,
        unique_name: str,
        title_key: str,
    ) -> None:
        """Initialiser le capteur."""
        super().__init__(coordinator)
        self._lang = lang
        self._category = category
        self._attr_name = ENTITY_TITLES.get(lang, ENTITY_TITLES["fr"])[title_key]
        self._attr_unique_id = f"{DOMAIN}_{unique_name}"
        self._attr_icon = "mdi:calendar-star"
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Ephemeride",
            manufacturer="WadohS",
            model="Ephemeride",
            sw_version=INTEGRATION_VERSION,
        )

    @property
    def state(self):
        """Retourner l'etat du capteur."""
        if not self.coordinator.data:
            return UNKNOWN_STATE.get(self._lang, UNKNOWN_STATE["fr"])

        if self._category is None:
            return self.coordinator.data.get(
                "saint_aujourdhui",
                UNKNOWN_STATE.get(self._lang, UNKNOWN_STATE["fr"]),
            )

        category_data = self._today_category_data
        return category_data.get("first") or UNKNOWN_STATE.get(self._lang, UNKNOWN_STATE["fr"])

    @property
    def extra_state_attributes(self):
        """Retourner les attributs additionnels."""
        if not self.coordinator.data:
            return {}

        data = self.coordinator.data
        if self._category is None:
            return {
                "saint_demain": data.get("saint_demain", UNKNOWN_STATE.get(self._lang, UNKNOWN_STATE["fr"])),
                "type_aujourdhui": data.get("type_aujourdhui"),
                "type_demain": data.get("type_demain"),
                "langue": data.get("langue", self._lang),
                "date": data.get("date", ""),
                "tous_saints_aujourdhui": data.get("tous_saints_aujourdhui", []),
                "tous_saints_demain": data.get("tous_saints_demain", []),
                "nombre_saints_aujourdhui": data.get("nombre_saints_aujourdhui", 0),
                "nombre_saints_demain": data.get("nombre_saints_demain", 0),
            }

        today = self._today_category_data
        tomorrow = self._tomorrow_category_data
        return {
            "categorie": self._category,
            "langue": data.get("langue", self._lang),
            "date": data.get("date", ""),
            "element_demain": tomorrow.get("first", UNKNOWN_STATE.get(self._lang, UNKNOWN_STATE["fr"])),
            "type_aujourdhui": today.get("first_type"),
            "type_demain": tomorrow.get("first_type"),
            "elements_aujourdhui": today.get("names", []),
            "elements_demain": tomorrow.get("names", []),
            "nombre_aujourdhui": today.get("count", 0),
            "nombre_demain": tomorrow.get("count", 0),
        }

    @property
    def _today_category_data(self) -> dict:
        details = self.coordinator.data.get("details_aujourdhui", {})
        by_category = details.get("by_category", {})
        return by_category.get(self._category, {})

    @property
    def _tomorrow_category_data(self) -> dict:
        details = self.coordinator.data.get("details_demain", {})
        by_category = details.get("by_category", {})
        return by_category.get(self._category, {})
