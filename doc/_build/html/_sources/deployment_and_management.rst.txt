Procédures de déploiement et de gestion de l'application
=========================================================

.. Note:: Voir aussi :doc:`Technologies <technologies>`

Déploiement de l'application à l'aide de la pipeline CI/CD de Circleci
-----------------------------------------------------------------------

Le projet *lettings* sur `Circleci <https://circleci.com/vcs-authorize/>`_ est lié au dépot github.

Les variables d'environnements du projet enregistrées dans *Project Settings* sont les suivantes: 

.. csv-table:: Variables d'environnement
   :header: "Nom", "Valeur"
   :widths: 15, 10

   "DOCKER_PASSWORD",	"mot_de_passe_dockerhub"
   "DOCKER_USERNAME",	"identifiant_dockerhub"
   "DSN",	"cle_sentry-DSN"
   "HEROKU_APP_NAME",	"lettings"
   "HEROKU_TOKEN",	"api_key_heroku*"
   "IMAGE_NAME",	"lettings_image"
   "SECRET_KEY",	"secret_key_django"


(*)L'API key est indiquée dans le `compte Heroku <https://dashboard.heroku.com/account>`_ dans *Account Settings*.

Le pipeline est configuré par le fichier *config.yml* situé dans le répertoire *.circleci* :

1. Les tests du projets sont lancés après l'installation des dépendances ;

2. Si les tests sont réussis, une image docker *lettings_image* est construite et poussée (push) ver le registre docker hub ;

3. Si l'image est bien construite, le déploiement se réalise sur héroku.

**Le pipeline se lance dès sa création puis à chaque commit sur Git hub.**. 

Le site web est en ligne à cette url publique : 

https://lettings-972532108750.herokuapp.com

Le pipeline CI/CD et ses builds sont visibles sur cette page : 

https://app.circleci.com/pipelines/github/Nunespace/Lettings 


Gestion de l'application
-------------------------

Surveillance des erreurs
^^^^^^^^^^^^^^^^^^^^^^^^
Sentry est utilisé comme outil de surveillance des erreurs. 
Chaque erreur est répertoriée dans le dossier *Issues* du projet sur Sentry : https://sentry.io


Gestion de la base de données
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 - Les données de l'API peuvent être administrées par le super-utilisateur avec le site d'administration de Django : 

https://lettings-972532108750.herokuapp.com/admin/

2 - Après avoir renseigné votre identifiant et votre mot de passe, ce site permet de `gérer toutes les opérations CRUD <https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django/7516605-effectuez-des-operations-crud-dans-ladministration-de-django>`_ sur les ressources de l'API.

.. Note:: Voir également :doc:`Interface de programmation d’application <api>`

Dans le cadre de la formation Python, un super-utilisateur est déjà créé dans la base de données Sqlite3 du projet.

