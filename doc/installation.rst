
Installation du projet
======================

Prérequisssssssssssssssss
------------
L'application aura besoin de **Python** (version 3.12), **Git** et **Pipenv** pour fonctionner. Si besoin, vous pouvez les installer en suivant les instructions sur `cette page`_.

.. _cette page: https://github.com/Nunespace/Lettings/blob/main/doc/installation_python-git-pipenv.md

Pour la surveillance des erreurs, vous aurez besoin de `créer un compte Sentry <https://sentry.io/signup/>`_. 



Installation du projet sur votre machine (local)
------------------------------------------------
Si vous souhaitez utiliser *pip* à la place de *pipenv*, vous diposez du fichier *requirements.txt* pour installer toutes les dépendances du projet. Il vous faudra ensuite activer vous-même l'environnement virtuel (dans ce cas enlever "pipenv" ou "pipenv run" de toutes les commandes),
et mettre *pip install* à la place de *pipenv install*

#. Ouvrez le **terminal** et tapez ::

    git clone https://github.com/Nunespace/Lettings.git

#. Placez-vous dans le répertoire Lettings ::

    cd Lettings

#. Installez les dépendances du projet ::

    pipenv install

#. Créer un fichier .env à la racine du projet, y mettre les variables suivantes [#f1]_ ::
    
    SECRET_KEY=votre_cle_secrète_django 
    DSN=votre_cle_DSN_sentry
    
#. Démarrer l'application avec ::

    pipenv run python manage.py runserver

#. Ouvrez votre navigateur et entrez l’URL comme indiqué sur le terminal pour démarrer l'application::

    http://127.0.0.1:8000/

#. Pour quitter le serveur, appuyez sur::

    CTRL+C


Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étape 5 et 6 à partir du répertoire racine du projet.

.. [#f1]

.. code-block::
   :caption: Pour créer une clé secrète Django, taper les commandes suivantes

       from django.core.management.utils import get_random_secret_key
       print(get_random_secret_key())



Création du projet sur sentry.io 
--------------------------------

1 - Sur votre compte Sentry, créer un projet Django

2 - Récupérer la clé client DSN de votre projet sentry [#f2]_

.. [#f2] Exemple de DSN :

 https://555555550faeed9ac552c37d085fec544@o4506343489601536.ingest.sentry.io/99999999999


