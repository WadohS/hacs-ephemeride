# Éphéméride - Notes du composant

Français | [English](README.md)

Ce dossier contient le composant Home Assistant `ephemeride`.

## Ce qu'il fait

- expose `sensor.saints_du_jour`
- expose des capteurs par categorie pour les saints, saintes, fetes, dates religieuses, prenoms et autres
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
- des objets, par exemple `[{"name": "Damien", "type": "saint"}]`

Le coordinator normalise tous les formats avant d'exposer les donnees du capteur et de classer chaque entree.

## Outils

- Audit de couverture : `python3 scripts/report_language_typing.py`
- Conversion d'un fichier : `python3 scripts/migrate_language_file.py <lang>`
- Ecriture reelle : `python3 scripts/migrate_language_file.py <lang> --write`
- Les fichiers de langue fournis utilisent maintenant partout des objets typés explicites

## Version

Version actuelle du composant : `1.4.4`
