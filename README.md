*** This Project is still on development. ***


This project needs Docker and docker-compose installed systemwide.
Please install docker and docker-compose to continue.


To build and run:

create .env file on /Backend/ directory with the following environmental variables set, for example:

# Django settings
SECRET_KEY = django-insecure-qa)1z*h^_*ty0=km7vr-ziqx4gct0%sm!=5d#gkw)60h*dg@d8
DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_PORT=3306
DB_ROOT_PASSWORD=root
# MySQL settings
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=Backend
MYSQL_USER=django
MYSQL_PASSWORD=django


create a .env file on /Frontend/ directory with the following environmental variables set:
WDS_SOCKET_PORT=3038


After those files are created, the next step is to run "docker-compose build" in the root directory of the project.
This will create the 4 containers used by the app. db, Backend, Frontend, and pythonCronjob


after the building is finished,
execute "docker-compose up" and it should start the services.
Go to "http://localhost:3038" to access the WebReport in ReactJS
Go to "http://localhost:8088" to access the DRF API REST


Feel free to contact me for further inquiries and suggestions.
