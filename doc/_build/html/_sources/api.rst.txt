Interface de programmation d’application (API)
===============================================

Le code est construit avec le framework web Django.
Il est composé de **trois applications** :

* **oc-lettings-site** où se trouve le fichier *settings.py* du projet Django et qui comporte un fichier *views* gérant les erreurs 404 et 500 ;
* **lettings** qui gèrent les modèles *Letting* et *Adress* ;
* **profiles** qui gère le modèle *Profiles*.


Pour utiliser l’interface de programmation (API) que Django met à disposition il existe deux possiblités.

Avec le shell interactif Python
-------------------------------

Pour lancer un shell Python, utilisez cette commande à la racine du projet :

``python manage.py shell``

Une fois dans le shell, explorez `l’API de base de données <https://docs.djangoproject.com/fr/5.0/intro/tutorial02/#playing-with-the-api>`_.

Django automatise entièrement la création des interfaces d’administration pour les modèles.


Avec le site d’administration de Django
---------------------------------------
Les données de l'API peuvent être administrées par le super-utilisateur avec le site d'administration de Django.
Ce site permet d'effectuer toutes les opérations CRUD (Create, Read, Update, Delete) sur les données de l'application.

Pour créer un super-utilisateur et explorer les fonctionnalités de l'interface d'administration, consulter `la documentation de Django <https://docs.djangoproject.com/fr/5.0/intro/tutorial02/#introducing-the-django-admin>`_. 

Dans le cadre de la formation Python (voir :doc:`Description du projet <description_project>`), un super-utilisateur est déjà créé et enregistré dans la base de données Sqlite3 du projet.