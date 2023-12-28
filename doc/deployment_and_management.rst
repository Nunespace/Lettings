Procédures de déploiement et de gestion de l'application
========================================================

Prérequis
---------

Disposer d'un compte sur :
- circleci : circleci.com/
- docker hub : hub.docker.com
- Heroku : www.heroku.com

Voir aussi le chapitre *Technologies*


Déploiement de l'application à l'aide de la pipeline CI/CD de circleci
---------------------------------------------------------------------

1 - Créer un projet sur heroku 

2 - Créer un projet sur circleci avec une dépot github

3 - Enregistrer les variables d'environnements du projet sur circleci : 

==============================================
    Name	                Value
==============================================
DOCKER_PASSWORD	votre_mot_de_pass_dockerhub	
DOCKER_USERNAME	votre identifiant_dockerhub	
DSN	            votre_cké_sentry-DSN	
HEROKU_APP_NAME	nom_de_votre_application_heroku .. exemple : lettings		
HEROKU_TOKEN	voir_ci_dessous_pour_l_obtenir
IMAGE_NAME	    ex:_lettings_image
SECRET_KEY	    votre_clé_secrète_django
===============================================
*pour obtenir HEROKU_TOKEN, taper dans votre terminal* : 
``heroku authorizations:create``
*Cela va récupérer un jeton, que vous devez utiliser comme variable HEROKU-TOKEN*

4 - La pipeline se lance dès sa création puis à chaque commit sur git hub.

Le site web est alors en ligne à cette url : https://nom_de_votre_application-nombre_attribué_par_heroku.herokuapp.com/
Exemple : https://lettings-972532108750.herokuapp.com/


