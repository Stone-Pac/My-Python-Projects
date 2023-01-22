import requests
import json
import logging

logging.basicConfig(level=logging.ERROR)

org_name = input("Enter your GitHub organization name: ")

def get_repositories(org_name):
    url = f'https://api.github.com/orgs/{org_name}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repos = json.loads(response.text)
        for repo in repos:
            print("Repository name: ", repo['name'])
            print("Repository URL: ", repo['html_url'])
            print("Created at: ", repo['created_at'])
            print("Updated at: ", repo['updated_at'])
            print("\n")
    else:
        logging.error(f'Error code: {response.status_code} Message: {response.text}')

get_repositories(org_name)
input("Press any key to exit")