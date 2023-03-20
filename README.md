deployed at https://aqueous-journey-63498.herokuapp.com/
relevant URLs

- https://aqueous-journey-63498.herokuapp.com/users
- https://aqueous-journey-63498.herokuapp.com/repos
- `https://aqueous-journey-63498.herokuapp.com/users/{username}/repos`

## Backend

### `gh_repos` (backend)

- `gh_repos/`: Django project files
  - `urls.py`: router
  - `settings`: configure things here, such as switching between mysql and dblite database
- `repos/`: Django app files
  - `models.py`: defines models
  - `serializers.py`: convert model instances to JSON so that the frontend can work with the received data
  - `views.py`- takes web requests
- `fixtures`: contains seed files
- `get_seed_data.py`: Python script that retrives user and repo information given usernames

### Create a virtual env

```
python3 -m pip install --user virtualenv
python3 -m venv env
cd env
source bin/activate
```

Installations

```
pip3 install django
pip3 install django-seed
pip3 install clean-text
pip3 install djangorestframework
python3 -m pip install django-cors-headers
pip3 install django-filter
pip3 install django-on-heroku
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

- go to localhost:8000
- go to localhost:8000/admin to view models & values (admin login needed)

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

### viewing the database using sqlite3

(was trying to use this for deployment but the sqlite file gets erased upon deployment from heroku)

https://sqlite.org/cli.html#zipdb

```
sqlite3 db.sqlite3
.tables
select * from repos_ghuser;
select count(*) from repos_repo;
```

### API Design Doc

not all of the APIs below are supported by the implemented server currently. This design doc outlines what the supported endpoints of a fully implemented server may look like.

- /users
  - GET: gets all users data
- /repos
  - GET: gets all repos data
  - POST: creates a new repo
- /user/{username}
  - GET: gets data of given user
  - PUT: upates fields (given via HTTP request body) of given user
  - DELETE: deletes user; not supported as requires authenitication from GitHub, and not going to be supported by design
  - POST: adds user. Also will require authentication and will not be supported by design
- /user/{username}/repos
  - GET: gets repos of given user
- /repo/{id}
  - GET: gets data of given repo, as identified by repo's primary key id
  - PUT: edits repo info, if applicable. Requires GitHub auth.
  - POST: N/A
  - DELETE: deletes repo. Requires auth and will not be supported by design.

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

from repos.models import GhUser, Repo
```

For how to use the API, see https://docs.djangoproject.com/en/4.1/intro/tutorial02/#playing-with-the-api

### Room for Future Improvements

- Make the database collation such that emojis are supported by the seeding process & mysql db (had to remove from repo descriptions for now due to incompatibility)
