# REVIEWS API TASK

"Entrance task for 1FIT"

API service that allows authorized users to add and retrieve reviews about any companies

## Installation

Use the package manager to install needed modules for virtualenv

And install following modules:

```bash
coverage==5.1
Django==3.0.7
django-ipware==2.1.0
django-nose==1.4.6
django-readme-generator==2019.9.7
djangorestframework==3.11.0
importlib-metadata==1.6.1
jsonmerge==1.7.0
jsonschema==3.2.0
load==2019.4.13
psycopg2-binary==2.8.5
pytest==5.4.3
sqlparse==0.3.1
```


## Creating an admin user

First we’ll need to create a user who can login to the admin site. Run the following command:

```bash
python manage.py createsuperuser
```

Enter your desired username and press enter.

```bash
Username: admin
```

You will then be prompted for your desired email address:

```bash
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```bash
Password: **********
Password (again): *********
Superuser created successfully.
```

## Api documentation

[link](https://documenter.getpostman.com/view/11714008/Szzn6G5x?version=latest)