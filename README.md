# Projet

Ce projet python permet de se connecter à une base de données et renvoie le statut de connexion à cette base de données.

## Lancer le projet avec Docker

`docker build -t projet-eval .`
`docker run projet-eval:latest`

## Lancer le projet en local (sans Docker)

`python -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`
`python app.py`