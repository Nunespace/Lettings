Procédures de déploiement et de gestion de l'application
=========================================================

Prérequis
---------

Disposer des identifiants et mots de passe pour :

* circleci : https://circleci.com/

* docker hub : https://hub.docker.com

* Heroku : https://www.heroku.com

.. Note:: Voir aussi :doc:`Technologies <technologies>`


Déploiement de l'application à l'aide de la pipeline CI/CD de circleci
-----------------------------------------------------------------------
1 - Installer Heroku CLI : https://devcenter.heroku.com/articles/heroku-cli

2 - Créer un projet sur circleci avec une dépot github

3 - Enregistrer les variables d'environnements du projet sur circleci : 


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


4 - **Le pipeline se lance dès sa création puis à chaque commit sur Git hub.**

Le site web est alors en ligne à cette url : 

https://lettings-972532108750.herokuapp.com

Le pipeline CI/CD et ses builds sont visibles sur cette page : 

https://app.circleci.com/pipelines/github/Nunespace/Lettings 


Gestion de l'application
-------------------------

Surveillance des erreurs
^^^^^^^^^^^^^^^^^^^^^^^^
Sentry est utilisé comme outil de surveillance des erreurs. 
Chaque erreur est répertoriée dans le dossier *Issues* du projet sur votre compte Sentry : https://sentry.io


Gestion de la base de données
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 - Les données de l'API peuvent être administrées par le super-utilisateur avec le site d'administration de Django : 

https://heroku_app_name-nombre_attribue_par_heroku.herokuapp.com/admin/

Exemple : https://lettings-972532108750.herokuapp.com/admin/

2 - Entrer votre identifiant et votre mot de passe pour accéder au site d'administration de Django : ce site permet de `gérer toutes les opérations CRUD <https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django/7516605-effectuez-des-operations-crud-dans-ladministration-de-django>`_ sur les ressources de l'API.

.. Note:: Voir également :doc:`Interface de programmation d’application <api>`

Dans le cadre de la formation Python, un superutilisateur est déjà créé dans la base de données Sqlite3 du projet.

