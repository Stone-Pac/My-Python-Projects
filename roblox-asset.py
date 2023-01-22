import requests
import traceback

def log_error(error):
    with open('error_log.txt', 'a') as f:
        f.write(error + '\n')

user_id = input("Enter the user ID: ")
asset_type_id = input("Enter the asset type ID: ")

url = f'https://inventory.roblox.com/v2/users/{user_id}/inventory/{asset_type_id}'

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data['data']:
            print(f'Asset ID: {item["assetId"]} - Asset Type: {item["assetTypeId"]}')
        input("Press Enter to close the window...")
    else:
        log_error(f'Error: {response.status_code}')
        print(f'Error: {response.status_code}')
except Exception as e:
    log_error(traceback.format_exc())
    print("An error has occurred, check error_log.txt for details")