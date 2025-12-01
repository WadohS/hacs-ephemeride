"""The Saints du Jour custom component."""
import logging

DOMAIN = "saints_du_jour"

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up the Saints du Jour component."""
    _LOGGER.info("Saints du Jour component is setting up.")
    
    # Vérifier si la plateforme 'sensor' est configurée
    if DOMAIN not in config:
        return True

    # Charger la plateforme 'sensor'
    hass.helpers.discovery.load_platform('sensor', DOMAIN, config[DOMAIN], config)
    
    return True
