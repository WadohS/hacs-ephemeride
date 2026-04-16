[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

_Intégration pour afficher les saints du jour, les saintes, les fêtes, les dates religieuses et les prénoms dans Home Assistant._

**Cette intégration créera les plateformes suivantes.**

Plateforme | Description
-- | --
`sensor` | Capteurs par catégorie : commémoration principale, saint, sainte, fête, date religieuse, prénom et autre

{% if not installed %}
## Installation

1. Cliquez sur installer.
2. Redémarrez Home Assistant
3. Configurez l'intégration :

[![Ajouter l'intégration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ephemeride)

Ou manuellement : allez dans "Configuration" -> "Intégrations", cliquez sur "+" et recherchez "Éphéméride".

{% endif %}

## Configuration via l'interface utilisateur

La configuration se fait entièrement via l'interface graphique :
- Sélectionnez votre langue parmi 6 langues disponibles
- Changez la langue à tout moment via les options de l'intégration
- Les données locales de chaque pays sont respectées
- Les catégories sont séparées pour faciliter les cartes et automatisations

## Langues supportées 🌍

- 🇫🇷 Français
- 🇬🇧 English
- 🇩🇪 Deutsch
- 🇪🇸 Español
- 🇮🇹 Italiano
- 🇵🇹 Português

## Les contributions sont les bienvenues !

Si vous souhaitez contribuer, veuillez lire les [Directives de contribution](CONTRIBUTING.md)

***

[releases-shield]: https://img.shields.io/github/release/WadohS/hacs-ephemeride.svg?style=for-the-badge
[releases]: https://github.com/WadohS/hacs-ephemeride/releases
[commits-shield]: https://img.shields.io/github/commit-activity/y/WadohS/hacs-ephemeride.svg?style=for-the-badge
[commits]: https://github.com/WadohS/hacs-ephemeride/commits/main
[license-shield]: https://img.shields.io/github/license/WadohS/hacs-ephemeride.svg?style=for-the-badge
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/hacs/integration
[maintenance-shield]: https://img.shields.io/badge/maintainer-WadohS-blue.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
