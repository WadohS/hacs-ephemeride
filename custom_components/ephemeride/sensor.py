"""Capteur pour l'intégration Éphéméride."""
import logging
from datetime import datetime

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import DOMAIN, CONF_LANGUAGE, SENSOR_NAME

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Configurer le capteur à partir d'une entrée de configuration."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    lang = entry.options.get(CONF_LANGUAGE, entry.data.get(CONF_LANGUAGE, "fr"))

    async_add_entities([EphemerideSensor(coordinator, entry, lang)])


class EphemerideSensor(CoordinatorEntity, SensorEntity):
    """Représentation du capteur Éphéméride."""

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

    @property
    def state(self):
        """Retourner l'état du capteur (saint d'aujourd'hui)."""
        return self.coordinator.data.get("today", "Inconnu")

    @property
    def extra_state_attributes(self):
        """Retourner les attributs additionnels."""
        data = self.coordinator.data
        today_date = datetime.now().strftime("%d/%m/%Y")
        tomorrow_date = (datetime.now()).strftime("%d/%m/%Y")
        
        attrs = {
            "saint_demain": data.get("tomorrow", "Inconnu"),
            "langue": self._lang,
            "date": today_date,
            "tous_saints_aujourdhui": [saint[0] for saint in data.get("today_all", [])],
            "tous_saints_demain": [saint[0] for saint in data.get("tomorrow_all", [])],
        }
        
        return attrs

    @property
    def available(self):
        """Retourner True si l'entité est disponible."""
        return self.coordinator.last_update_success
