"""Intégration Éphéméride pour Home Assistant."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from datetime import timedelta, datetime
import json
import os

from .const import DOMAIN, CONF_LANGUAGE

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup(hass: HomeAssistant, config: dict):
    """Setup non config flow (possible si besoin)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Configurer l'intégration à partir de config flow."""
    lang = entry.options.get(CONF_LANGUAGE, entry.data.get(CONF_LANGUAGE, "fr"))

    async def async_update_data():
        """Récupérer les données du saint du jour."""
        today = datetime.now().strftime("%m-%d")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%m-%d")
        
        try:
            # Construire le chemin vers le fichier de langue
            file_path = os.path.join(
                os.path.dirname(__file__), 
                "languages", 
                f"{lang}.json"
            )
            
            _LOGGER.debug(f"Lecture du fichier: {file_path}")
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Récupérer le premier saint de la journée
            today_saints = data.get(today, [["Inconnu", "Saint"]])
            tomorrow_saints = data.get(tomorrow, [["Inconnu", "Saint"]])
            
            return {
                "today": today_saints[0][0] if today_saints else "Inconnu",
                "tomorrow": tomorrow_saints[0][0] if tomorrow_saints else "Inconnu",
                "today_all": today_saints,
                "tomorrow_all": tomorrow_saints,
            }
        except FileNotFoundError:
            _LOGGER.error(f"Fichier de langue non trouvé: {file_path}")
            return {
                "today": "Erreur",
                "tomorrow": "Erreur",
                "today_all": [],
                "tomorrow_all": [],
            }
        except Exception as e:
            _LOGGER.error(f"Erreur lors de la lecture des données: {e}")
            return {
                "today": "Erreur",
                "tomorrow": "Erreur",
                "today_all": [],
                "tomorrow_all": [],
            }

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_interval=timedelta(hours=1),
        update_method=async_update_data,
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Enregistrer le listener pour les changements d'options
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Nettoyer à la suppression."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Recharger l'intégration quand les options changent."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
