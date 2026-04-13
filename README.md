# Ephemeride - Home Assistant Integration

[Français](README.fr.md) | English

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![Community Forum][forum-shield]][forum]

_Home Assistant integration that exposes the saint of the day and upcoming feast day with multilingual support._

[![Open in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-ephemeride&category=integration)

![Ephemeride icon](https://raw.githubusercontent.com/WadohS/hacs-ephemeride/main/custom_components/ephemeride/icon.png)

## Features

This integration creates the following platform:

Platform | Description
-- | --
`sensor` | Sensor exposing the main saint of the day and related attributes

### `sensor.saint_du_jour`

- State: main saint of the current day
- Attributes:
  - `saint_demain`: tomorrow's main saint
  - `langue`: configured language
  - `date`: current local date in Home Assistant timezone
  - `tous_saints_aujourdhui`: full list for today, limited to 5 items
  - `tous_saints_demain`: full list for tomorrow, limited to 5 items
  - `nombre_saints_aujourdhui`: total number of entries today
  - `nombre_saints_demain`: total number of entries tomorrow

## Supported Languages

- French (`fr`)
- English (`en`)
- German (`de`)
- Spanish (`es`)
- Italian (`it`)
- Portuguese (`pt`)

## Installation

### HACS

1. Open HACS in Home Assistant
2. Go to `Integrations`
3. Open the menu in the top-right corner and choose `Custom repositories`
4. Add `https://github.com/WadohS/hacs-ephemeride`
5. Select the `Integration` category
6. Search for `Ephemeride` and install it
7. Restart Home Assistant

### Manual installation

1. Copy `custom_components/ephemeride` into your Home Assistant `custom_components/` directory
2. Restart Home Assistant

## Configuration

Configuration is fully handled from the UI:

1. Go to `Settings` -> `Devices & Services`
2. Click `Add integration`
3. Search for `Ephemeride`
4. Select the language you want
5. Submit the form

To change the language later:

1. Open the `Ephemeride` integration card
2. Click `Configure`
3. Select the new language
4. Submit the form

The integration reloads automatically when the language is updated.

## Lovelace Example

```yaml
type: entity
entity: sensor.saint_du_jour
name: Saint of the day
icon: mdi:calendar-star
```

## Automation Example

```yaml
automation:
  - alias: "Saint of the day notification"
    trigger:
      - platform: time
        at: "08:00:00"
    action:
      - service: notify.mobile_app
        data:
          title: "Saint of the day"
          message: "Today we celebrate {{ states('sensor.saint_du_jour') }}"
```

## Development Notes

- Language data is stored in `custom_components/ephemeride/languages/`
- UI translations are stored in `custom_components/ephemeride/translations/`
- The integration supports both legacy tuple-like entries and plain string lists in language files

## Changelog

### Version 1.2.5
- Fixed option changes so switching language reloads the integration correctly
- Fixed date handling to use the Home Assistant timezone instead of raw system time
- Updated documentation in French and English

### Version 1.2.4
- Added official icons and logos
- Improved compatibility between coordinator data and sensor state handling

### Version 1.2.3
- Fixed JSON compatibility across supported language formats
- Fixed unknown state issues on `sensor.saint_du_jour`
- Limited large state attributes to avoid recorder size issues

## Support

If you hit a bug, please open an issue with:

- Home Assistant version
- Integration version
- Selected language
- Detailed description
- Relevant logs

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
