
Installation du projet
======================

Prérequis
------------
L'application aura besoin de **Python** (version 3.12), **Git** et **Pipenv** pour fonctionner. Si besoin, vous pouvez les installer en suivant les instructions sur `cette page`_.

.. _cette page: https://github.com/Nunespace/Lettings/blob/main/doc/installation_python-git-pipenv.md



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
    
    SECRET_KEY=cle_secrète_django 
    DSN=cle_DSN_sentry

    
#. Démarrez le serveur avec ::

    pipenv run python manage.py runserver

#. Ouvrez votre navigateur et entrez l’URL comme indiqué sur le terminal pour démarrer l'application web : http://127.0.0.1:8000/ ou http://localhost:8000/


#. Pour quitter le serveur, appuyez sur *CTRL+C*


Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étape 5 et 6 à partir du répertoire racine du projet.


.. [#f1] 

.. note:: Les clés secrètes Django et DSN de Sentry sont communiquées en dehors du dépôt Git hub
    Pour récupérer clé DSN de Sentry : aller sur le `compte Sentry <https://sentry.io>`_, puis dans le projet *lettings*, ouvrir *Project Settings*.
    
   