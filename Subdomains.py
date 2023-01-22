import requests
from bs4 import BeautifulSoup

url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=roblox.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
subdomains = soup.find_all('subdomains')

for subdomain in subdomains:
    print(subdomain.text)

input("Press Enter to exit...")