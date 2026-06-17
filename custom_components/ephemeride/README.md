# Ephemeride - Component Notes

[Français](README.fr.md) | English

This directory contains the Home Assistant custom component for `ephemeride`.

## What it does

- exposes `sensor.saints_du_jour`
- exposes category sensors for saints, female saints, feasts, religious dates, given names and others
- supports six language datasets
- lets the user change language from the UI
- reloads automatically after an options change

## File layout

```text
custom_components/ephemeride/
|- __init__.py
|- config_flow.py
|- const.py
|- manifest.json
|- sensor.py
|- languages/
`- translations/
```

## Data formats

Language files may contain either:

- plain string lists, for example `["Mary", "Joseph"]`
- tuple-like lists, for example `[["Marie", "Sainte"], ["Jour de l'an", "Fete"]]`
- object entries, for example `[{"name": "Damian", "type": "saint"}]`

The coordinator normalizes all formats before exposing sensor data and classifying each entry.

## Tooling

- Coverage audit: `python3 scripts/report_language_typing.py`
- Convert one file: `python3 scripts/migrate_language_file.py <lang>`
- Write changes in place: `python3 scripts/migrate_language_file.py <lang> --write`
- Shipped language files now use explicit typed objects everywhere

## Version

Current component version: `1.4.1`
