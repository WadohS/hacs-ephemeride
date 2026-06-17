# Ephemeride - Home Assistant Integration

[Français](README.fr.md) | English

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![Community Forum][forum-shield]][forum]

_Home Assistant integration that exposes the visible commemorations of the day with dedicated sensors for saints, female saints, feasts, religious dates, given names and other events._

[![Open in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-ephemeride&category=integration)

![Ephemeride icon](https://raw.githubusercontent.com/WadohS/hacs-ephemeride/main/custom_components/ephemeride/icon.png)

## Features

This integration creates the following platform:

Platform | Description
-- | --
`sensor` | Sensors exposing the day's commemorations plus dedicated category sensors

### `sensor.saints_du_jour`

- State: list of the day's commemorations, limited to 5 entries
- Attributes:
  - `saint_demain`: tomorrow's main saint
  - `commemoration_principale_aujourdhui`: today's first entry
  - `commemoration_principale_demain`: tomorrow's first entry
  - `langue`: configured language
  - `date`: current local date in Home Assistant timezone
  - `tous_saints_aujourdhui`: full list for today, limited to 5 items
  - `tous_saints_demain`: full list for tomorrow, limited to 5 items
  - `nombre_saints_aujourdhui`: total number of entries today
  - `nombre_saints_demain`: total number of entries tomorrow

### Additional sensors

- `sensor.saint_du_jour`
- `sensor.sainte_du_jour`
- `sensor.fete_du_jour`
- `sensor.date_religieuse_du_jour`
- `sensor.prenom_du_jour`
- `sensor.autre_du_jour`

Each category sensor displays the matching entries for today, limited to 5 items, and also exposes the primary entry for today and tomorrow in its attributes. Untyped entries remain in `sensor.autre_du_jour` until the corresponding language file provides explicit metadata. Given names can now be isolated in `sensor.prenom_du_jour` instead of being mixed with saints.

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
entity: sensor.saints_du_jour
name: Saints of the day
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
          title: "Saints of the day"
          message: "Today we celebrate {{ states('sensor.saints_du_jour') }}"
```

## Development Notes

- Language data is stored in `custom_components/ephemeride/languages/`
- UI translations are stored in `custom_components/ephemeride/translations/`
- Local branding is shipped in `custom_components/ephemeride/brand/`
- The integration supports plain string lists, tuple-like entries and object entries in language files
- Country-specific calendars are preserved and classified at runtime without forcing a single shared dataset

### Progressive language migration

- Coverage audit: `python3 scripts/report_language_typing.py`
- Convert one file to explicit objects: `python3 scripts/migrate_language_file.py fr`
- Write the converted file back: `python3 scripts/migrate_language_file.py fr --write`
- Converted entries use `name` and `type`, and keep `source_type` when the original file already carried a business-specific label
- All shipped language files are now stored as explicit typed objects

## Changelog

### Version 1.4.1
- Restore the last known sensor state and attributes after Home Assistant restarts until fresh ephemeris data is loaded again

### Version 1.4.0
- Add a dedicated `prenom` sensor category and expand shipped name-day datasets across all supported languages
- Rename the main saint entities to match their real role and migrate legacy Home Assistant entity ids on reload
- Show all visible commemorations in sensor states instead of collapsing each day to the first entry only

### Version 1.3.3
- Fully convert all shipped language files to explicit typed objects
- Improve automatic typing heuristics so saints, saintes and feasts are populated across all supported languages

### Version 1.3.2
- Add progressive migration tools to audit and type language files without losing country-specific calendars

### Version 1.3.1
- Add yearly computation of movable liturgical dates and merge them with country-specific calendars at runtime
- Improve category detection so liturgical and feast sensors are populated more consistently

### Version 1.3.0
- Added dedicated sensors for male saints, female saints, feasts, religious dates and other commemorations
- Added local integration branding for recent Home Assistant versions
- Added a language file validation script

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
