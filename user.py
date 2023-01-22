import requests

username = input("Enter your GitHub username: ")

def get_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        with open("response.txt", "w") as f:
            f.write(response.text)
        for repo in repos:
            print("Repository name: ", repo['name'])
            print("Repository URL: ", repo['html_url'])
            print("Created at: ", repo['created_at'])
            print("Number of files: ", repo['size'])
            print("Number of directories: ", repo['forks'])
            print("\n")
    else:
        print(f'Error code: {response.status_code} Message: {response.text}')

get_repositories(username)
input("Press any key to exit")