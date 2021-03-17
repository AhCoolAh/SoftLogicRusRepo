# Getting Started with server

### Database

1. Install postgesql 12. Create database and user as its owner using username, password and db name as the following:
        'NAME': 'MapDB',
        'USER': 'postgres',
        'PASSWORD': 'ThePassword'

### Server

1. Create virtual environment inside server folder and activate it. Ubuntu example below:

```
$ sudo apt install virtualenv
$ virtualenv env
$ source env/bin/activate
```

Add Your venv folder to .gitignore file.

2. Install all requirements from requirements.txt. Use pip3

```
$ pip3 install -r requirements.txt
```

3. Make migrations

```
$ python manage.py makemigrations
$ python manage.py migrate
```

4. Run script to fill database with data

```
$ python generation.py 
```

5. Run server

```
$ python manage.py runserver
```