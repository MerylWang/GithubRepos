
## Backend 
### `gh_repos` (backend)
- `gh_repos`: Django project files 
- `repos`: Django app files 
- `fixtures`: contains seed files 
- `get_seed_data.py`: Python script that retrives user and repo information given usernames

### Create a virtual env 
```
python3 -m pip install --user virtualenv

python3 -m venv env
cd env
source bin/activate
```

### Installations
```
pip3 install django
pip3 install django-seed
pip3 install clean-text
pip3 install djangorestframework
python3 -m pip install django-cors-headers
pip3 install django-filter
```

Creating the project & app 
```
python3 -m django startproject gh_repos
python3 manage.py startapp repos
```

start the server locally: 
```
python3 manage.py runserver
# http://127.0.0.1:8000/
```

### Seeding the Database locally 
0. Run migrations to create datable tables based on the models in `models.py`
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    - `makemigrations` observes changes made to models in `models.py` and creates a corresponding migration file in `./repos/migrations`
    - `migrate` applies unapplied migration files. 

1. run `get_seed_data.py` to create JSON files of seed data, which are retrived using Github API. 
    The seed data is outputted to `fixtures/<filename>.json`

2. Seed the database using the files
    ```
    python3 manage.py loaddata ./fixtures/ghuser.json
    python3 manage.py loaddata ./fixtures/repo.json
    ```

### Resources: 
Github API: 
https://stateful.com/blog/github-api-list-repositories
https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-a-user

Seeding the DB: 
https://medium.com/@ardho/migration-and-seeding-in-django-3ae322952111
https://docs.djangoproject.com/en/4.1/howto/initial-data/

Writing an API Server in Django: 
https://www.django-rest-framework.org/api-guide/serializers/
https://docs.djangoproject.com/en/4.1/topics/http/views/


### Other 
Django version: 4.1.7 
```
python3 -m django --version
4.1.7
```

To enter the Django console 
```
python3 manage.py shell
```
For commands interacting with the API, see https://docs.djangoproject.com/en/4.1/intro/tutorial02/#playing-with-the-api


### Room for Future Improvements
- Make collation such as emojis are supported by the seeding process & mysql db (had to remove from repo descriptions for now due to incompatibility)

### TODOs
- to deploy the database, connect to Heroku ClearDB or other hosted MYSQL DB, or import as a dblite file 

