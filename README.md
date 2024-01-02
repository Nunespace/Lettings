# Application web Orange County Lettings 

***
Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. 
Elle souhaite améliorer son site tant sur le code que sur le déploiement.

## Amélioration de l'application

 Les améliorations suivantes ont été mise en oeuvre:
- Refonte de l'architecture modulaire dans le repository GitHub ;
- Réduction de diverses dettes techniques sur le projet ;
- Ajout d'un pipeline CI/CD ainsi que son déploiement ; 
- Surveillance de l’application et suivi des erreurs via Sentry ; 
- Création de la documentation technique de l'application avec Read The Docs et Sphinx.


## Prérequis

L'application aura besoin de **Python** (version 3.12), **Git** et **Pipenv** pour fonctionner. Si besoin, vous pouvez les installer en suivant les instructions sur [cette page](doc/installation_python-git-pipenv.md).


## Installation

Cette application exécutable localement peut être installée à l'aide de *pipenv* en suivant les étapes décrites ci-dessous.
> [!NOTE]  
> Si vous souhaitez utiliser *pip* à la place de *pipenv*, vous diposez du fichier *requirements.txt* pour installer toutes les dépendances du projet. Il vous faudra ensuite activer vous-même l'environnement virtuel (dans ce cas enlever "pipenv" ou "pipenv run" de toutes les commandes),
et mettre *pip install* à la place de *pipenv install*


1. Ouvrez le **terminal** et tapez ::
```
git clone https://github.com/Nunespace/Lettings.git
```

2. Placez-vous dans le répertoire Lettings :
```
cd Lettings
```

3. Installez les dépendances du projet :
```
pipenv install
```
4. Créer un fichier .env à la racine du projet, y mettre les variables suivantes[^1] :
```
SECRET_KEY=cle_secrète_django 
DSN=cle_DSN_sentry
```
    
5. Démarrez l'application avec :
```
pipenv run python manage.py runserver
```
6. Ouvrez votre navigateur et entrez l’URL comme indiqué sur le terminal pour démarrer l'application :

http://127.0.0.1:8000/

7. Pour quitter le serveur, appuyez sur *CTRL+C*


Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étape 5 et 6 à partir du répertoire racine du projet.

## Documentation

La documentation complète de ce projet est consultable ici : [Documentation](https://lettings17.readthedocs.io/fr/latest/)

## Déploiement

Le chapitre [*"Procédures de déploiement et de gestion de l’application" de la documentation*](https://lettings17.readthedocs.io/fr/latest/deployment_and_management.html) présente un récapitulatif haut niveau du fonctionnement du déploiement, la configuration requise ainsi que les étapes nécessaires pour l'effectuer.

## Tests et linting


### Lancement des tests
Les tests de ce projet ont été écrits avec le framework pytest.

Ils sont executables avec la commande [^2]: 
```
pipenv run pytest
```

### Couverture de test

Ce projet contient la librairie Python Coverage.py qui fournit un rapport qui nous donne le pourcentage de couverture de ligne par fichier source de couverture. Ce rapport peut être obtenu avec cette commande[^1] : 
```
pipenv run pytest --cov=.
```
Un rapport HTML, plus détaillé, peut aussi être généré en tapant[^2] : 
```
pipenv run pytest --cov=. --cov-report html
```
Un nouveau dossier *htmlcov* est ainsi créé à l'endroit où vous avez lancé la commande. Avec votre navigateur, ouvrez le fichier *index.html*  qui contient un résumé du rapport de couverture. À partir de cette page, vous pourrez naviguer à travers les différents fichiers afin d’avoir le détail sur la couverture.


### Linting

Le linting sur l'ensemble du code peut être exécuté avec Flake8.

Exécutez, à partir de la  racine du projet, la commande suivante[^2] : 
```
pipenv run flake8
```

[^1]: L’application nécessite un fichier *.env*, qui contient la clé secrète Django et la clé DSN de Sentry, non présent dans ce dépôt github.
[^2]: Si vous utilisez *pip*, activer votre environnement virtuel et enlever *pipenv run* : 



