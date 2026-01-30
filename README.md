# 🖥️ API de Gestion de Serveurs (Test)

Une API RESTful légère construite avec **FastAPI**. Ce projet permet de gérer un parc de serveurs virtuel via des opérations CRUD (Create, Read, Update, Delete) avec une persistance des données dans un fichier JSON local.

## 📌 Fonctionnalités
- **Lister** tous les serveurs enregistrés.
- **Créer** un nouveau serveur (avec validation d'ID unique).
- **Modifier** les informations d'un serveur existant (RAM, IP, nom, etc.).
- **Supprimer** un serveur via son identifiant.

---

## 🛠️ Installation et Mise en place

### 1. Prérequis
**Python 3.7+** et **pip** installés.

### 2. Configuration de l'environnement
Ouvrez un terminal dans le dossier du projet :

```bash
# Création de l'environnement virtuel
python3 -m venv venv

# Activation de l'environnement
source venv/bin/activate

# Installation des dépendances nécessaires
pip install fastapi uvicorn
```

Lien Postman des tests effectués : https://fabienbll-6871878.postman.co/workspace/Fabien-BALLEREAU's-Workspace~356f19cf-779d-4c41-8c38-3266ded02599/collection/51921490-988145bf-3c84-4aa8-8f7b-59c0ddfb54d9?action=share&creator=51921490
