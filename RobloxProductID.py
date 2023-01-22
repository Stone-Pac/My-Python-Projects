import requests

def get_product_info(product_id):
    url = f"https://api.roblox.com/marketplace/productinfo?assetId={product_id}"
    response = requests.get(url)
    data = response.json()
    name = data["Name"]
    price = data["PriceInRobux"]
    icon_url = data["IconUrl"]
    creator_id = data["Creator"]["Id"]
    creator_name = data["Creator"]["Name"]
    return name, price, icon_url, creator_id, creator_name

while True:
    product_id = input("Enter a product ID: ")
    name, price, icon_url, creator_id, creator_name = get_product_info(product_id)

    print("Name:", name)
    print("Price:", price)
    print("Icon URL:", icon_url)
    print("Creator ID:", creator_id)
    print("Creator Name:", creator_name)