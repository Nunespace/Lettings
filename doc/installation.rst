Installation du projet
======================

Prérequis
------------
L'application aura besoin de **Python** (version 3.12), **Git** et **Pipenv** pour fonctionner. Si besoin, vous pouvez les installer en suivant les instructions sur [cette page](docs/installation_python-git-pipenv.md).
Pour la surveillance des erreurs, vous aurez besoin de créer un compte sentry : https://sentry.io/signup/
 
Création du projet sur sentry.io 
--------------------------------

1 - Sur votre compte Sentry, créer un projet Django

2 - Récupérer la clé client DSN de votre projet sentry (exemple de DSN :https://555555550faeed9ac552c37d085fec544@o4506343489601536.ingest.sentry.io/99999999999)

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

4. Créer un fichier .env à la racine du projet, y mettre les variables suivantes:
``
SECRET_KEY=votre_clé_secrète_django
DSN=votre_clé_DSN_sentry
``


5. Démarrer l'application avec :

.. code-block:: console
    
    pipenv run python manage.py runserver

6. Ouvrez votre navigateur et entrez l’URL suivante : [http://127.0.0.1:8000/](http://127.0.0.1:8000/) comme indiqué sur le terminal pour démarrer l'application.

7. Pour quitter le serveur, appuyez sur ` CTRL+C `

Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étape 5 et 6 à partir du répertoire racine du projet.


Pour créer une clé secrète Django, taper les commandes suivantes :
``
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
``