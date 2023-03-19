"""
Create a Python script that:
a. Takes one or more GitHub usernames
b. Gets a list of the public repositories for that user.
c. For each user and repo, create corresponding json blob, and write to seed file 

Some room for future improvements: 
- if an user has more than `PER_PAGE` public repos, add logic in place to increment page number until all repos are grabbed
"""
import requests
import json 
from cleantext import clean

USERNAMES = ['MerylWang', 'kyle8998', 'reliu375', 'ehavugi']
APP_NAME = 'repos'
PER_PAGE = 35
BASE_URL = 'https://api.github.com/users/{username}/repos?per_page={per_page}'
FILES_PATH = './fixtures'

ghuser_json = []
repo_json = []

for username in USERNAMES:
    req = BASE_URL.format(username=username, per_page=PER_PAGE)
    r = requests.get(req).json()

    owner_json = r[0]["owner"]
    ghuser_id = owner_json["id"]
    ghuser_json.append({
        "model": '{}.ghuser'.format(APP_NAME), 
        "pk": ghuser_id, 
        "fields": {
          "username": owner_json["login"], 
          "html_url": owner_json["html_url"]
        }
    })

    for repo_dict in r:
        repo_json.append({
            "model": '{}.repo'.format(APP_NAME),
            "pk": repo_dict['id'], 
            "fields": {
              "name": repo_dict['name'], 
              "description": clean(repo_dict['description'], no_emoji=True), 
              "language": repo_dict['language'], 
              "stargazers_count": repo_dict['stargazers_count'], 
              "forks_count": repo_dict['forks_count'], 
              "html_url": repo_dict['html_url'], 
              "owner_id": ghuser_id
            }
        })

with open("{}/ghuser.json".format(FILES_PATH), 'w') as f:
    json.dump(ghuser_json, f, indent=4)

with open("{}/repo.json".format(FILES_PATH), 'w') as f:
    json.dump(repo_json, f, indent=4)


