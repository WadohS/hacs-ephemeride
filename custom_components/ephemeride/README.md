# Éphéméride - Intégration Home Assistant

![Version](https://img.shields.io/badge/version-1.2.3-blue.svg)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-compatible-green.svg)
![Languages](https://img.shields.io/badge/languages-6-orange.svg)

## Description

L'intégration **Éphéméride** permet d'afficher le saint du jour et les festivités dans Home Assistant, avec support multilingue pour 6 langues différentes.

## 🌍 Langues supportées

- 🇫🇷 **Français** (fr)
- 🇬🇧 **English** (en)
- 🇩🇪 **Deutsch** (de)
- 🇪🇸 **Español** (es)
- 🇮🇹 **Italiano** (it)
- 🇵🇹 **Português** (pt)

## ✨ Fonctionnalités

- **Saint du jour** : Affiche le saint correspondant à la date actuelle
- **Saint de demain** : Prévision pour le jour suivant
- **Saints multiples** : Liste tous les saints et fêtes d'une journée
- **Configuration simple** : Interface graphique pour choisir la langue
- **Mise à jour automatique** : Rafraîchissement toutes les heures
- **Changement de langue** : Modification possible sans réinstallation

## 📦 Installation

### Via HACS (recommandé)

1. Ouvrez HACS dans Home Assistant
2. Allez dans "Intégrations"
3. Cliquez sur les trois points en haut à droite
4. Sélectionnez "Dépôts personnalisés"
5. Ajoutez l'URL : `https://github.com/WadohS/hacs-ephemeride`
6. Recherchez "Éphéméride" et installez-le
7. Redémarrez Home Assistant

### Installation manuelle

1. Copiez le dossier `custom_components/ephemeride` dans votre dossier `config/custom_components/`
2. Redémarrez Home Assistant

## ⚙️ Configuration

1. Allez dans **Configuration** → **Intégrations**
2. Cliquez sur **+ Ajouter une intégration**
3. Recherchez **Éphéméride**
4. Sélectionnez votre langue préférée
5. Cliquez sur **Soumettre**

## 📊 Utilisation

### Entité capteur

Une fois configurée, l'intégration crée une entité capteur :

**`sensor.saint_du_jour`**

### État et attributs

- **État** : Nom du saint principal du jour
- **Attributs** :
  - `saint_demain` : Saint de demain
  - `langue` : Langue configurée
  - `date` : Date actuelle
  - `tous_saints_aujourdhui` : Liste de tous les saints du jour
  - `tous_saints_demain` : Liste de tous les saints de demain

### Exemple dans Lovelace

```yaml
type: entity
entity: sensor.saint_du_jour
name: Saint du jour
icon: mdi:calendar-star
```

### Exemple d'automatisation

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
          message: "Nous fêtons {{ states('sensor.saint_du_jour') }} aujourd'hui !"
```

## 🔧 Modification de la langue

Pour changer la langue après installation :

1. Allez dans **Configuration** → **Intégrations**
2. Trouvez **Éphéméride**
3. Cliquez sur **Options**
4. Sélectionnez la nouvelle langue
5. Cliquez sur **Soumettre**

L'intégration se rechargera automatiquement avec la nouvelle langue.

## 📁 Structure des fichiers

```
custom_components/ephemeride/
├── __init__.py          # Initialisation de l'intégration
├── sensor.py            # Entité capteur
├── config_flow.py       # Configuration UI
├── const.py             # Constantes
├── manifest.json        # Métadonnées
├── languages/           # Données des saints par langue
│   ├── fr.json
│   ├── en.json
│   ├── de.json
│   ├── es.json
│   ├── it.json
│   └── pt.json
└── translations/        # Traductions de l'interface
    ├── fr.json
    ├── en.json
    ├── de.json
    ├── es.json
    ├── it.json
    └── pt.json
```

## 📋 Format des données

Les fichiers JSON dans `languages/` suivent ce format :

```json
{
  "01-01": [["Marie", "Sainte"], ["Jour de l'an", "Fête"]],
  "02-14": [["Valentin", "Saint"]],
  ...
}
```

Chaque date (format `MM-DD`) contient un tableau de paires `[nom, type]` où :
- `nom` : Nom du saint ou de la fête
- `type` : "Saint", "Sainte" ou "Fête" (adapté à chaque langue)

## 🐛 Signaler un problème

Si vous rencontrez un bug ou avez une suggestion :

1. Vérifiez que vous utilisez la dernière version
2. Consultez les [issues existantes](https://github.com/WadohS/hacs-ephemeride/issues)
3. Créez une nouvelle issue avec :
   - Version de Home Assistant
   - Version de l'intégration
   - Langue configurée
   - Description détaillée du problème
   - Logs pertinents

## 📝 Changelog

### Version 1.2.3
- ✨ Ajout de 5 nouvelles langues (en, de, es, it, pt)
- 🌍 Support multilingue complet
- 🔄 Possibilité de changer de langue sans réinstallation
- 📚 Interface utilisateur traduite dans toutes les langues
- 🐛 Corrections mineures

### Version 1.0.0
- 🎉 Version initiale
- 🇫🇷 Support du français uniquement

## 👨‍💻 Contributeurs

- [@WadohS](https://github.com/WadohS) - Créateur et mainteneur

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

Merci à la communauté Home Assistant pour leur support et leurs contributions !

---

**Note** : Cette intégration utilise des données de saints et fêtes adaptées aux traditions culturelles de chaque pays/langue. Les dates et noms peuvent varier selon les calendriers liturgiques locaux.
