
# TP222 – Gestion d Articles

#Nom: NDZESSA EMMANUEL FREDY
#Matricule: 24F2868

## Description du projet
TP222 est une application web simple pour gérer des produits (ou articles) avec les fonctionnalités suivantes :  

- Création, lecture, modification et suppression (CRUD) des produits.  
- Recherche de produits par titre, auteur ou catégorie.  
- Interface utilisateur simple avec formulaires pour chaque action.

---
## Lien du Projet
(https://site-de-blog-1.onrender.com)

## Langages et technologies utilisés

### Backend
- **Python 3**  
- **Flask** : Framework web léger pour Python  
- **Flask-SQLAlchemy** : ORM pour gérer la base de données  
- **Gunicorn** : Serveur WSGI pour le déploiement

### Frontend
- **HTML** pour les templates  
- **Jinja2** pour le rendu dynamique des templates avec Flask  
- **Tailwin** pour le style (si applicable)

### Base de données
- **SQLite** : base de données locale, utilisée via SQLAlchemy  
  - Stockée dans le dossier `instance/` (`instance/database.db`)  
  - Pas besoin de serveur externe pour ce TP  

---

## Structure du projet
TP222/
│
├── App.py # Fichier principal Flask
├── requirements.txt # Dépendances Python
├── runtime.txt # Version de Python pour le déploiement (ex: Python-3.12.3)
├── Procfile # Commande de démarrage pour Render (ex: gunicorn App:app)
├── instance/ # Dossier contenant la base de données SQLite
│ └── database.db
├── env/ # Dossier pour l’environnement virtuel local (optionnel)
├── templates/ # Dossier des fichiers HTML
│ ├── home.html
│ ├── create.html
│ ├── modify.html
│ ├── read.html
│ └── search.html
└── static/ # (optionnel) dossier pour CSS, JS ou images


---

## Endpoints (Routes)

| Route                     | Méthode | Description                           |
|----------------------------|---------|---------------------------------------|
| `/`                        | GET     | Page d’accueil, liste tous les produits |
| `/create`                  | GET/POST| Créer un nouveau produit              |
| `/update/<int:id_post>`    | GET/POST| Modifier un produit existant          |
| `/delete/<int:id_post>`    | GET     | Supprimer un produit                  |
| `/read/<int:id_post>`      | GET     | Afficher les détails d’un produit     |
| `/search`                  | GET/POST| Rechercher des produits par mot-clé   |

---

## Installation et utilisation en local

1. **Cloner le projet**
```bash
git clone <git@github.com:NDZESSAEMMANUEL/Site_de_blog.git>
cd TP222
```
2. **creer et active l environnemnt **
```bash
python3 -m venv env
source env/bin/activate   # Linux / Mac
# env\Scripts\activate    # Windows
```
3. **installer les riquirements **
```bash
pip install -r requirements.txt
```
4. **Lancer en locale**
```bash
python App.py
```
4. **Lancer en Production**
```bash
gunicorn App:app
```
## Déploiement sur Render

1. **Créer un compte** sur [Render](https://render.com) et créer un nouveau service “Web Service”.  

2. **Choisir le dépôt GitHub** contenant ton projet.  

3. **Branch à déployer** : `main`  

4. **Root Directory** : laisser vide si `App.py` est à la racine du projet.  

5. **Build Command** :  
```bash
pip install -r requirements.txt
```
6. **Start Command ** :  
```bash
gunicorn App:app
```
Environment Variables :
SECRET_KEY : une chaîne aléatoire pour sécuriser Flask (ex: monsecret123)
DATABASE_URL : laisser vide ou ne pas définir si vous utilisez SQLite localement
Fichiers de configuration pour le déploiement :
runtime.txt : version de Python (ex: python-3.12.3)
Procfile : commande de démarrage (web: gunicorn App:app)
instance/ : contient la base de données SQLite (database.db)
.env ou env/ : variables d’environnement et environnement virtuel (optionnel pour local)
Cliquer sur Deploy
Render construira automatiquement le projet et lancera Gunicorn
L’application sera accessible via l’URL fournie par Render (ex : https://tp222.onrender.com)

Pour toute modification future, il suffit de committer et push sur GitHub, puis de redeployer sur Render.
