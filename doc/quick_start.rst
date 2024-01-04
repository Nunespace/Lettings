Démarrage rapide
===================

Avec le terminal et Python
--------------------------

Une fois le projet installé en local (voir :doc:`Installation du projet <installation>`)

1. Démarrez l'application avec :

``pipenv run python manage.py runserver``

2. Pour démarrer l'application web, ouvrez votre navigateur et entrez l’URL suivante : http://127.0.0.1:8000/

3. Pour quitter le serveur, appuyez sur *CTRL+C*


Avec Docker
-----------

1. Aller sur l'url de recherche de `Docker Hub <https://hub.docker.com/search/?type=image&image_filter=official>`_

2. Dans la zone de recherche, taper *nunespace/lettings*

3. Cliquer sur l'image puis sur l'onglet *Tags*

4. Copier/coller la commande "Docker Pull Command" dans votre terminal

5. Dans votre Docker Desktop, l'image se trouve alors dans *Images/local*

6. Cliquer sur *Run*, donner un nom à votre conteneur et taper 8000 dans *host port*

7. Cliquer sur *Run* puis sur 8000:8000⁠ ou ouvrez votre navigateur et entrez l’URL suivante: http://localhost:8000/

