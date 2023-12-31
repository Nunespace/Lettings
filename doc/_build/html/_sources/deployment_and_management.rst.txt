Procédures de déploiement et de gestion de l'application
=========================================================

Prérequis
---------

Disposer d'un compte sur :

* circleci : https://circleci.com/
* docker hub : https://hub.docker.com
* Heroku : https://www.heroku.com

.. Note:: Voir aussi :doc:`Technologies <technologies>`


Déploiement de l'application à l'aide de la pipeline CI/CD de circleci
-----------------------------------------------------------------------
1 - Installer Heroku CLI : https://devcenter.heroku.com/articles/heroku-cli

2 - Créer un projet sur circleci avec une dépot github

3 - Enregistrer les variables d'environnements du projet sur circleci : 

.. table:: Truth table for "not"
   :widths: auto

    +------------------+-----------------------------+
    | Name	       | Value                       |
    +==================+=============================+
    | DOCKER_PASSWORD  | votre_mot_de_pass_dockerhub |
    +------------------+-----------------------------+
    | DOCKER_USERNAME  | votre identifiant_dockerhub |
    +------------------+-----------------------------+
    | DSN	       | votre_cké_sentry-DSN        |
    +------------------+-----------------------------+
    | HEROKU_APP_NAME  | nom_de_application_heroku   |
    +------------------+-----------------------------+
    | HEROKU_TOKEN     | votre identifiant_dockerhub |
    +------------------+-----------------------------+
    | IMAGE_NAME       | nom_de_l_image              |
    +------------------+-----------------------------+
    | SECRET_KEY       | Cle_secrete_django          |
    +------------------+-----------------------------+


.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3


HEROKU_APP_NAME : Exemple : lettings

*pour obtenir HEROKU_TOKEN, taper dans votre terminal* : 
``heroku authorizations:create``
*Cela va récupérer un jeton, que vous devez utiliser comme variable HEROKU-TOKEN*

4 - La pipeline se lance dès sa création puis à chaque commit sur git hub.

Le site web est alors en ligne à cette url : https://nom_de_votre_application-nombre_attribué_par_heroku.herokuapp.com/
Exemple : https://lettings-972532108750.herokuapp.com/


Gestion de l'application
-------------------------

Surveillance des erreurs
Sentry est utilisé comme outil de surveillance des erreurs. 
Chaque erreur est répertoriée dans le dossier *Issues* du projet sur votre compte Sentry : https://sentry.io


Gestion de la base de données
-----------------------------

1 - Les données de l'API peuvent être administrées par le super-utilisateur avec le site d'administration de Django : <https://heroku_app_name-nombre_attribué_par_heroku.herokuapp.com/admin/>`_
Exemple : https://lettings-972532108750.herokuapp.com/admin/

2 - Entrer votre identifiant et votre mot de passe pour accéder au site d'administration de Django : ce site permet de gérer toutes les opérations [CRUD](<https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django/7516605-effectuez-des-operations-crud-dans-ladministration-de-django>`_) sur les ressources de l'API.

::Rem:
Voir également :doc:`Interface de programmation d’application <api>`

-Dans le cadre de la formation Python, un superutilisateur est déjà créé dans la base de données Sqlite3 du projet.*

