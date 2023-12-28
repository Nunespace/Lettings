Installation du projet
======================

Prérequis
------------
L'application aura besoin de **Python** (version 3.12), **Git** et **Pipenv** pour fonctionner. Si besoin, vous pouvez les installer en suivant les instructions sur [cette page](docs/installation_python-git-pipenv.md).


Installation du projet sur votre machine (local)
------------
Si vous souhaitez utiliser pip à la place de pipenv, vous diposez du fichier *requirements.txt* pour installer toutes les dépendances du projet. Il vous faudra ensuite activer vous-même l'environnement virtuel (dans ce cas enlever "pipenv" ou "pipenv run" de toutes les commandes).

1. Ouvrez le terminal et tapez :

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

 
4. Démarrer l'application avec :
```
pipenv run python manage.py runserver
```
5. Ouvrez votre navigateur et entrez l’URL suivante : [http://127.0.0.1:8000/](http://127.0.0.1:8000/) comme indiqué sur le terminal pour démarrer l'application.

6. Pour quitter le serveur, appuyez sur ` CTRL+C `

Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étape 4 et 6 à partir du répertoire racine du projet.

