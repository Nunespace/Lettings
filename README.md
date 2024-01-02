# Application web Orange County Lettings 

***
Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. 
Elle souhaite améliorer son site tant sur le code que sur le déploiement.

## Fonctionnalités de l'application

L'application permettra de gérer une base de données pour stocker et manipuler de manière sécurisée les informations de leurs clients, ainsi que les contrats et les événements qu'Epic Events organise.
L’application est faite en ligne de commande. Le principe du moindre privilège est appliqué lors de l'attribution de l'accès aux données.
Une journalisation est mise en oeuvre avec Sentry pour:
- toutes les exceptions inattendues, 
- chaque création/modiﬁcation d’un collaborateur,
- la signature d’un contrat.

 
## Configuration actuelle

L’application nécessite un fichier config.ini non présent dans ce dépôt github.

## Prérequis

L'application aura besoin de **Python** (version 3.12), **Git** et **Pipenv** pour fonctionner. Si besoin, vous pouvez les installer en suivant les instructions sur [cette page](doc/installation_python-git-pipenv.md).


## Installation

Cette application exécutable localement peut être installée à l'aide de pipenv en suivant les étapes décrites ci-dessous.
> [!NOTE]  
> Si vous souhaitez utiliser *pip* à la place de *pipenv*, vous diposez du fichier *requirements.txt* pour installer toutes les dépendances du projet. Il vous faudra ensuite activer vous-même l'environnement virtuel (dans ce cas enlever "pipenv" ou "pipenv run" de toutes les commandes),
et mettre *pip install* à la place de *pipenv install*


#. Ouvrez le **terminal** et tapez ::
```
git clone https://github.com/Nunespace/Lettings.git
```

#. Placez-vous dans le répertoire Lettings ::
```
cd Lettings
```

#. Installez les dépendances du projet ::
```
pipenv install
```
#. Créer un fichier .env à la racine du projet, y mettre les variables suivantes [#f1]_ ::
```
SECRET_KEY=cle_secrète_django 
DSN=cle_DSN_sentry
```
    
#. Démarrer l'application avec ::
```
pipenv run python manage.py runserver
```
#. Ouvrez votre navigateur et entrez l’URL comme indiqué sur le terminal pour démarrer l'application::

http://127.0.0.1:8000/

#. Pour quitter le serveur, appuyez sur *CTRL+C*


Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étape 5 et 6 à partir du répertoire racine du projet.

## Documentation

La documentation complète de ce projet est consultable ici : [Documentation](https://lettings17.readthedocs.io/fr/latest/)

## Déploiement

Le chapitre [*"Procédures de déploiement et de gestion de l’application" de la documentation*](https://lettings17.readthedocs.io/fr/latest/deployment_and_management.html) présente : 
● un récapitulatif haut niveau du fonctionnement du déploiement ;
● la configuration requise ;
● les étapes nécessaires pour effectuer le déploiement.

## Tests et linting


### Lancement des tests
Les tests de ce projet ont été écrits avec le framework pytest.

Ils sont executables avec la commande : 
```
pipenv run pytest
```

### Couverture de test

Ce projet contient la librairie Python Coverage.py qui fournit un rapport qui nous donne le pourcentage de couverture de ligne par fichier source de couverture. Ce rapport peut être obtenu avec cette commande : 
```
pipenv run pytest --cov=.
```
Un rapport HTML, plus détaillé, peut aussi être généré en tapant : 
```
pipenv run pytest --cov=. --cov-report html
```
Nn nouveau dossier *htmlcov* est ainsi créé à l'endroit où vous avez lancé la commande. Avec votre navigateur, ouvrez le fichier *index.html*  qui contient un résumé du rapport de couverture. À partir de cette page, vous pourrez naviguer à travers les différents fichiers afin d’avoir le détail sur la couverture.


### Linting
Le linting peut être exécuté avec Flake8.
Exécuter, à partir de la  racine du projet, la commande suivante : 
```pipenv run flake8```

Si vous utilisez pip, activer votre environnement virtuel, puis taper simplement : 
```flake8```





