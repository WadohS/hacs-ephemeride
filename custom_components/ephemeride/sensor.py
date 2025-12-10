"""Capteur pour l'integration Ephemeride."""
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.helpers.entity import DeviceInfo

from .const import DOMAIN, CONF_LANGUAGE, SENSOR_NAME

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Configurer le capteur a partir d'une entree de configuration."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    lang = entry.options.get(CONF_LANGUAGE, entry.data.get(CONF_LANGUAGE, "fr"))

    async_add_entities([EphemerideSensor(coordinator, entry, lang)])


class EphemerideSensor(CoordinatorEntity, SensorEntity):
    """Representation du capteur Ephemeride."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        entry: ConfigEntry,
        lang: str,
    ):
        """Initialiser le capteur."""
        super().__init__(coordinator)
        self._lang = lang
        self._attr_name = "Saint du jour"
        self._attr_unique_id = f"{DOMAIN}_{SENSOR_NAME}"
        self._attr_icon = "mdi:calendar-star"
        self._attr_has_entity_name = True
        
        # Device info for better integration
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Ephemeride",
            manufacturer="WadohS",
            model="Ephemeride",
            sw_version="1.2.2",
        )

    @property
    def state(self):
        """Retourner l'etat du capteur (saint d'aujourd'hui)."""
        if not self.coordinator.data:
            return "Inconnu"
        return self.coordinator.data.get("saint_aujourdhui", "Inconnu")

    @property
    def extra_state_attributes(self):
        """Retourner les attributs additionnels."""
        if not self.coordinator.data:
            return {}
        
        data = self.coordinator.data
        
        attrs = {
            "saint_demain": data.get("saint_demain", "Inconnu"),
            "langue": data.get("langue", self._lang),
            "date": data.get("date", ""),
            "tous_saints_aujourdhui": data.get("tous_saints_aujourdhui", []),
            "tous_saints_demain": data.get("tous_saints_demain", []),
            "nombre_saints_aujourdhui": data.get("nombre_saints_aujourdhui", 0),
            "nombre_saints_demain": data.get("nombre_saints_demain", 0),
        }
        
        return attrs
