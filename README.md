# GithubRepos
ADI fulltstack exercise

### Installations
```
pip3 install django-seed
pip3 install clean-text
```

### Seeding the Database locally 
0. Run migrations to create datable tables based on the models in `models.py`
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    `makemigrations` observes changes made to models in `models.py` and creates a corresponding migration file in `./repos/migrations`
    `migrate` applies unapplied migration files. 

1. run `get_seed_data.py` to create JSON files of seed data, which are retrived using Github API. 
    The seed data is outputted to `fixtures/<filename>.json`

2. Seed the database using the files
    ```
    python3 manage.py loaddata ./fixtures/ghuser.json
    python3 manage.py loaddata ./fixtures/repo.json
    ```



to deploy, connect to Heroku ClearDB or other hosted MYSQL DB 
or import as a dblite file 

### Resources: 
Github API: 
https://stateful.com/blog/github-api-list-repositories
https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-a-user

Seeding the DB: 
https://medium.com/@ardho/migration-and-seeding-in-django-3ae322952111
https://docs.djangoproject.com/en/4.1/howto/initial-data/


### Other 
Django version: 4.1.7 
```
python3 -m django --version
4.1.7
```

To start the server locally: 
```
python3 manage.py runserver
# http://127.0.0.1:8000/
```

Creating the project & app 
```
python3 -m django startproject gh_repos
python3 manage.py startapp repos
```

### Room for Future Improvements
- Make collation such as emojis are supported by the seeding process & mysql db (had to manually remove from repo descriptions due to incompatibility for now)
