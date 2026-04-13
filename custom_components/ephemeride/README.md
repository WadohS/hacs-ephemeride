# Ephemeride - Component Notes

[Français](README.fr.md) | English

This directory contains the Home Assistant custom component for `ephemeride`.

## What it does

- exposes `sensor.saint_du_jour`
- exposes category sensors for saints, female saints, feasts, religious dates and others
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

## Version

Current component version: `1.3.0`
