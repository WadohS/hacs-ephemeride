# Éphéméride - Intégration Home Assistant

Français | [English](README.md)

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![Community Forum][forum-shield]][forum]

_Intégration Home Assistant qui expose le saint du jour et celui du lendemain avec support multilingue._

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-ephemeride&category=integration)

![Icône Éphéméride](https://raw.githubusercontent.com/WadohS/hacs-ephemeride/main/custom_components/ephemeride/icon.png)

## Fonctionnalités

Cette intégration crée la plateforme suivante :

Plateforme | Description
-- | --
`sensor` | Capteur exposant le saint principal du jour et ses attributs associés

### `sensor.saint_du_jour`

- État : saint principal du jour
- Attributs :
  - `saint_demain` : saint principal du lendemain
  - `langue` : langue configurée
  - `date` : date locale courante selon le fuseau Home Assistant
  - `tous_saints_aujourdhui` : liste complète du jour, limitée à 5 entrées
  - `tous_saints_demain` : liste complète du lendemain, limitée à 5 entrées
  - `nombre_saints_aujourdhui` : nombre total d'entrées aujourd'hui
  - `nombre_saints_demain` : nombre total d'entrées demain

## Langues supportées

- Français (`fr`)
- Anglais (`en`)
- Allemand (`de`)
- Espagnol (`es`)
- Italien (`it`)
- Portugais (`pt`)

## Installation

### HACS

1. Ouvrez HACS dans Home Assistant
2. Allez dans `Intégrations`
3. Ouvrez le menu en haut à droite puis `Dépôts personnalisés`
4. Ajoutez `https://github.com/WadohS/hacs-ephemeride`
5. Sélectionnez la catégorie `Integration`
6. Recherchez `Ephemeride` puis installez l'intégration
7. Redémarrez Home Assistant

### Installation manuelle

1. Copiez `custom_components/ephemeride` dans le dossier `custom_components/` de Home Assistant
2. Redémarrez Home Assistant

## Configuration

La configuration se fait entièrement via l'interface :

1. Ouvrez `Paramètres` -> `Appareils et services`
2. Cliquez sur `Ajouter une intégration`
3. Recherchez `Ephemeride`
4. Sélectionnez la langue souhaitée
5. Validez

Pour changer la langue plus tard :

1. Ouvrez la carte d'intégration `Ephemeride`
2. Cliquez sur `Configurer`
3. Sélectionnez la nouvelle langue
4. Validez

L'intégration se recharge automatiquement après changement de langue.

## Exemple Lovelace

```yaml
type: entity
entity: sensor.saint_du_jour
name: Saint du jour
icon: mdi:calendar-star
```

## Exemple d'automatisation

```yaml
automation:
  - alias: "Notification saint du jour"
    trigger:
      - platform: time
        at: "08:00:00"
    action:
      - service: notify.mobile_app
        data:
          title: "Saint du jour"
          message: "Nous fêtons {{ states('sensor.saint_du_jour') }} aujourd'hui"
```

## Notes de développement

- Les données calendaires sont dans `custom_components/ephemeride/languages/`
- Les traductions UI sont dans `custom_components/ephemeride/translations/`
- L'intégration supporte les anciens formats type tuple et les listes simples dans les fichiers de langue

## Changelog

### Version 1.2.5
- Correction du changement de langue via les options avec rechargement correct de l'intégration
- Correction de la gestion de date pour utiliser le fuseau horaire Home Assistant
- Mise à jour de la documentation en français et en anglais

### Version 1.2.4
- Ajout des icônes et logos officiels
- Amélioration de la compatibilité entre les données du coordinator et l'état du capteur

### Version 1.2.3
- Correction de compatibilité JSON entre plusieurs formats de fichiers de langue
- Correction de l'état inconnu sur `sensor.saint_du_jour`
- Limitation des attributs volumineux pour éviter les erreurs Recorder

## Support

Si tu rencontres un bug, ouvre une issue avec :

- version de Home Assistant
- version de l'intégration
- langue sélectionnée
- description détaillée
- logs utiles

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
