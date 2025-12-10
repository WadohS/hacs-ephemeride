"""Capteur pour l'integration Ephemeride."""
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

# Limite de securite pour les attributs (en caracteres)
MAX_SAINTS_IN_ATTRIBUTES = 50


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

    @property
    def state(self):
        """Retourner l'etat du capteur (saint d'aujourd'hui)."""
        return self.coordinator.data.get("today", "Inconnu")

    @property
    def extra_state_attributes(self):
        """Retourner les attributs additionnels."""
        data = self.coordinator.data
        today_date = datetime.now().strftime("%d/%m/%Y")
        
        # Recuperer les listes de saints
        today_all = data.get("today_all", [])
        tomorrow_all = data.get("tomorrow_all", [])
        
        # Limiter le nombre de saints pour eviter de depasser 16KB
        today_saints_list = [saint[0] for saint in today_all[:MAX_SAINTS_IN_ATTRIBUTES]]
        tomorrow_saints_list = [saint[0] for saint in tomorrow_all[:MAX_SAINTS_IN_ATTRIBUTES]]
        
        attrs = {
            "saint_demain": data.get("tomorrow", "Inconnu"),
            "langue": self._lang,
            "date": today_date,
            "tous_saints_aujourdhui": today_saints_list,
            "tous_saints_demain": tomorrow_saints_list,
            "nombre_saints_aujourdhui": len(today_all),
            "nombre_saints_demain": len(tomorrow_all),
        }
        
        # Avertissement si la liste est tronquee
        if len(today_all) > MAX_SAINTS_IN_ATTRIBUTES:
            attrs["note"] = f"Liste limitee a {MAX_SAINTS_IN_ATTRIBUTES} saints pour optimiser les performances"
        
        return attrs

    @property
    def available(self):
        """Retourner True si l'entite est disponible."""
        return self.coordinator.last_update_success

    @property
    def device_info(self):
        """Informations sur le peripherique."""
        return {
            "identifiers": {(DOMAIN, "ephemeride")},
            "name": "Ephemeride",
            "manufacturer": "WadohS",
            "model": "Saint du jour",
            "sw_version": "1.2.0",
        }
