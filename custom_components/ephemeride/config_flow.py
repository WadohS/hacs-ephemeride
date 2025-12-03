"""Config flow pour l'intégration Éphéméride."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import CONF_LANGUAGE, DOMAIN, SUPPORTED_LANGUAGES


class EphemerideConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestion de la configuration via UI."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Retourner le flux d'options."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Gérer l'étape de configuration initiale."""
        # Vérifier qu'une seule instance existe
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="Éphéméride", data=user_input)

        # Dictionnaire des langues avec leurs noms complets
        language_options = {
            "fr": "Français",
            "en": "English",
            "de": "Deutsch",
            "es": "Español",
            "it": "Italiano",
            "pt": "Português"
        }

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_LANGUAGE, default="fr"):
                    vol.In(language_options)
            })
        )


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Gestion des options de configuration."""

    def __init__(self, config_entry: config_entries.ConfigEntry):
        """Initialiser le flux d'options."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Gérer les options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Dictionnaire des langues avec leurs noms complets
        language_options = {
            "fr": "Français",
            "en": "English",
            "de": "Deutsch",
            "es": "Español",
            "it": "Italiano",
            "pt": "Português"
        }

        # Récupérer la langue actuelle
        current_lang = self.config_entry.options.get(
            CONF_LANGUAGE,
            self.config_entry.data.get(CONF_LANGUAGE, "fr")
        )

        schema = vol.Schema({
            vol.Required(CONF_LANGUAGE, default=current_lang):
                vol.In(language_options)
        })

        return self.async_show_form(step_id="init", data_schema=schema)
