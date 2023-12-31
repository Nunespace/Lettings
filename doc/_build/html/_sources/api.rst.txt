Interface de programmation d’application (API)
===============================================

Le code est construit avec le framework web Django.
Il est composé de trois applications :

* oc-lettings-site où se trouve le fichier settings.py du projet Django et qui comporte un fichier views gérant les errurs 404 et 500
* lettings qui gèrent les modèles *Letting* et *Adress*
* profiles qui gère le modèle *Profiles*


Pour utiliser l’interface de programmation (API) que Django met à disposition il existe deux possiblités. L'

Avec le shell interactif Python
-------------------------------

Pour lancer un shell Python, utilisez cette commande à la racine du projet :

``python manage.py shell``

Une fois dans le shell, explorez l’API de base de données:

    https://docs.djangoproject.com/fr/5.0/intro/tutorial02/#playing-with-the-api

Django automatise entièrement la création des interfaces d’administration pour les modèles.


Avec le site d’administration de Django
---------------------------------------
Les données de l'API peuvent être administrées par le super-utilisateur avec le site d'administration de Django.
Ce site permet d'effectuer toutes les opérations CRUD (Create, Read, Update, Delete) sur les données de l'application.

Pour créer un super-utilisateur et explorer les fonctionnalités de l'interface d'administration, visiter le site Django à cette adresse : 
    https://docs.djangoproject.com/fr/5.0/intro/tutorial02/#introducing-the-django-admin

*rem : Dans le cadre de la formation Python, un superutilisateur est déjà créé et enregistré dans la base de données Sqlite3 du projet.*