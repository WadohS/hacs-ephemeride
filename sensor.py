"""Sensor platform for Saints du Jour."""
import logging
import json
import os
from datetime import date

from homeassistant.helpers.entity import Entity
from homeassistant.util import dt as ha_dt
from dateutil.easter import easter
from datetime import timedelta

_LOGGER = logging.getLogger(__name__)

# Le chemin vers le fichier JSON est relatif au répertoire du composant
CURRENT_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CURRENT_DIR, 'ephemeris_corrected.json')

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Saints du Jour sensor platform."""
    
    # Charger les données et les adapter
    ephemeris_data = {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            for key, value in raw_data.items():
                # La structure de l'utilisateur est ["Name", "Type"]
                # On l'adapte à notre structure interne [[Name, Type]]
                if isinstance(value, list) and len(value) == 2 and isinstance(value[0], str):
                    ephemeris_data[key] = [value]
                else:
                    # Si la structure est déjà une liste de listes, on la garde (pour les fêtes mobiles)
                    ephemeris_data[key] = value
    except FileNotFoundError:
        _LOGGER.error("Ephemeris data file not found at %s", DATA_FILE)
        return
    except json.JSONDecodeError:
        _LOGGER.error("Error decoding ephemeris data from %s", DATA_FILE)
        return

    add_entities([SaintsDuJourSensor(ephemeris_data)], True)

class SaintsDuJourSensor(Entity):
    """Representation of a Saints du Jour Sensor."""

    def __init__(self, ephemeris_data):
        """Initialize the sensor."""
        self._state = None
        self._attributes = {}
        self._ephemeris_data = ephemeris_data
        self._name = "Saint du Jour"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return 'mdi:calendar-star'

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    def _get_saints_for_date(self, target_date):
        """Récupère la liste des saints/fêtes pour une date donnée."""
        year = target_date.year
        
        # 1. Fêtes Mobiles (basées sur Pâques)
        mobile_feasts_list = []
        paques = easter(year)
        
        # Définition des fêtes mobiles par rapport à Pâques
        mobile_feasts = {
            paques - timedelta(days=47): ["Mardi Gras", "Fête Mobile"],
            paques - timedelta(days=46): ["Mercredi des Cendres", "Fête Mobile"],
            paques - timedelta(days=7): ["Dimanche des Rameaux", "Fête Mobile"],
            paques - timedelta(days=3): ["Jeudi Saint", "Fête Mobile"],
            paques - timedelta(days=2): ["Vendredi Saint", "Fête Mobile"],
            paques - timedelta(days=1): ["Samedi Saint", "Fête Mobile"],
            paques: ["Pâques", "Fête Mobile"],
            paques + timedelta(days=1): ["Lundi de Pâques", "Fête Mobile"],
            paques + timedelta(days=39): ["Ascension", "Fête Mobile"],
            paques + timedelta(days=49): ["Pentecôte", "Fête Mobile"],
            paques + timedelta(days=50): ["Lundi de Pentecôte", "Fête Mobile"],
            paques + timedelta(days=60): ["Fête-Dieu", "Fête Mobile"],
        }
        
        # Vérifier si la date correspond à une fête mobile
        if target_date in mobile_feasts:
            mobile_feasts_list.append(mobile_feasts[target_date])

        # 2. Fêtes Fixes (MM-DD)
        date_key = target_date.strftime("%m-%d")
        fixed_saints_list = self._ephemeris_data.get(date_key, [])
        
        # Combiner les listes : Fêtes Mobiles en premier, puis Fêtes Fixes
        saints_list = mobile_feasts_list + fixed_saints_list
        
        return saints_list

    def _process_saints_data(self, saints_list, target_date, prefix=""):
        """Traite la liste des saints et retourne les attributs."""
        attributes = {}
        
        if saints_list:
            # Le premier saint/fête est l'état principal
            main_saint_name, main_saint_type = saints_list[0]
            
            # Créer la liste complète des noms pour l'attribut 'all_saints'
            all_saints_names = [f"{s_type} {s_name}" for s_name, s_type in saints_list]
            
            # Créer la chaîne de caractères pour l'attribut 'full_name'
            full_name_str = ", ".join([s_name for s_name, s_type in saints_list])
            
            attributes[f'{prefix}saint'] = main_saint_name
            attributes[f'{prefix}type'] = main_saint_type
            attributes[f'{prefix}full_name'] = full_name_str
            attributes[f'{prefix}all_saints'] = all_saints_names
            attributes[f'{prefix}count'] = len(saints_list)
            
        else:
            attributes[f'{prefix}saint'] = "Aucun"
            attributes[f'{prefix}type'] = "Aucun"
            attributes[f'{prefix}full_name'] = "Aucun saint ou fête"
            attributes[f'{prefix}all_saints'] = []
            attributes[f'{prefix}count'] = 0
            
        attributes[f'{prefix}date'] = target_date.strftime("%d/%m")
        
        return attributes

    def update(self):
        """Fetch new state data for the sensor."""
        today = ha_dt.now().date()
        tomorrow = today + timedelta(days=1)
        
        # 1. Données du jour
        today_saints = self._get_saints_for_date(today)
        today_attributes = self._process_saints_data(today_saints, today)
        
        # Mise à jour de l'état principal
        self._state = today_attributes.pop('saint')
        self._attributes = today_attributes
        
        # 2. Données du lendemain
        tomorrow_saints = self._get_saints_for_date(tomorrow)
        tomorrow_attributes = self._process_saints_data(tomorrow_saints, tomorrow, prefix="next_day_")
        
        # Ajout des attributs du lendemain
        self._attributes.update(tomorrow_attributes)

