# Django Intro with Postgres

This project contain a introduction to Django with Postgres.

## Configure the project

1. Clone the project with
```bash
git clone https://github.com/PedroLuisDionisioFraga/S203-Django-Project.git
```
2. Create a virtual environment
```bash
python3 -m venv venv
```
3. Install the requirements
```bash
pip install -r Backend/requirements.txt
```
4. Create a Postgres container:
   1. Download `docker desktop` from [here](https://www.docker.com/products/docker-desktop).
   2. Run the script to create the container or, if already created, to start it:
   ```bash
   Database/database_S203.sh
   ```

## Configure the database
1. Start and execute the container using the script:
```bash
Database/database_S203.sh
```
2. Create the database called `"database S203"`:
```bash
create database "database S203";
3. Connect to the database:
```bash
\c "database S203"
```

## Get Started

### Creating a base of the project
First of all, you need to start the virtual environment (venv):
```bash
Backend/venv/bin/activate
```
Now we are going to create a django project running the following command:
```bash
django-admin startproject messages
```
The folder structure of django will be created:
├─ messages
│  ├─ manage.py
│  └─ messages
│     ├─ __init__.py
│     ├─ asgi.py
│     ├─ settings.py
│     ├─ urls.py
│     └─ wsgi.py

The folder explanation is:
- `message`: It's our project folder. In fact, you can even rename it if he wants.
- `manage.py`: You will do almost everything in your project!
- `asgi.py`: If you decide to serve your application using ASGI (asynchronous Python) this is the
entry-point;
- `settings.py`: The Django project configuration. You'll be doing a lot in this script;
- `urls.py`: The declaration of your project's routes (or URLs);
- `wsgi.py`: If you decide to serve your application using WSGI (Gunicorn, for example) this
is the entry point;

Now we are created the app:
```bash
python manage.py startapp board
```
The folder structure of the app will be created:
board
  ├─ migrations
  └─ __init__.py
  ├─ __init__.py
  ├─ admin.py
  ├─ apps.py
  ├─ models.py
  ├─ tests.py
  └─ views.py

- `admin.py`: Used to display your model in the Django admin panel. It's a basic CRUD.
- `apps.py`: For you to create configurations of your application.
- `models.py`: For you to create the model of your application. The classes that represent entities. Changes here need to be synchronized with the database through migrations.
- `tests.py`: Here you create the application tests.
- `views.py`: Here you create the views or the application's responses to URLs.

### Connection with the database

1. Configure the database variables:
In the `Backend/messages/messages/settings.py` file, find to the `DATABASES` variable and change the `ENGINE` to `django.db.backends.postgresql` and the `NAME` to `database S203`:
```python
DATABASES = {
   "default": {
      "ENGINE": "django.db.backends.postgresql",
      "NAME": "database S203",
      "USER": "root",
      "PASSWORD": "root",
      "HOST": "localhost",
      "PORT": "5432",
   }
}
```

2. Sync the apps with the database.
If you start the project running:
```bash
python manage.py runserver
```

NOTE: When you run the command, it starts the Django development server to run your application. If you see a message like:
```bash
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
To see the changes run the command and you are see:
```bash
\dt
 List of relations
| Schema | Name                       | Type  | Owner    |
| ------ | -------------------------- | ----- | -------- |
| public | auth_group                 | table | postgres |
| public | auth_group_permissions     | table | postgres |
| public | auth_permission            | table | postgres |
| public | auth_user                  | table | postgres |
| public | auth_user_groups           | table | postgres |
| public | auth_user_user_permissions | table | postgres |
| public | django_admin_log           | table | postgres |
| public | django_content_type        | table | postgres |
| public | django_migrations          | table | postgres |
| public | django_session             | table | postgres |
(10 rows)
```


### Creating the model
Let’s start with the `message` entity. Edit the `models.py` script in the `board` folder and add the following code:
```python
class Message(models.Model):
  title = models.CharField(max_length=100, blank=False)
  data = models.DateTimeField(auto_now_add=True)
  text = models.TextField
  author = models.ForeignKey('auth.User', related_name='recados', on_delete=models.CASCADE)
```

In Django, a model's id field is an auto-incrementing primary key that is automatically created unless you define your own primary key. The models class provides various field types:

* `title`: A CharField requiring input, max length of 100 characters.
* `date`: A DateTimeField set to the date and time when the record was created.
* `text`: A TextField for unlimited text.
* `author`: A ForeignKey field to the auth_user table, establishing a one-to-many relationship. If the referenced user is deleted, this record will also be deleted.

Now we are going to create a `Follower` entity.
```python
class Follower(models.Model):
  follower_user = models.ForeignKey('auth.User', related_name='+',
  on_delete=models.CASCADE)
  followed_user = models.ForeignKey('auth.User', related_name='+', on_delete=models.CASCADE)
```

To create the necessary migrations after alter the models, run the command:
```bash
python manage.py makemigrations board
```

NOTE: You can see the SQL creation commands running the command:
```bash
python manage.py sqlmigrate board 0001
```