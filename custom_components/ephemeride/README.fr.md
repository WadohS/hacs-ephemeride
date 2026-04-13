# Éphéméride - Notes du composant

Français | [English](README.md)

Ce dossier contient le composant Home Assistant `ephemeride`.

## Ce qu'il fait

- expose `sensor.saint_du_jour`
- prend en charge six jeux de données linguistiques
- permet de changer la langue depuis l'interface
- recharge automatiquement l'intégration après modification des options

## Structure

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

## Formats de donnees

Les fichiers de langue peuvent contenir :

- des listes simples, par exemple `["Mary", "Joseph"]`
- des listes type tuple, par exemple `[["Marie", "Sainte"], ["Jour de l'an", "Fete"]]`

Le coordinator normalise les deux formats avant d'exposer les donnees du capteur.

## Version

Version actuelle du composant : `1.2.5`
