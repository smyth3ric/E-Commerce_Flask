import requests

def test():
    
    url = f'https://botw-compendium.herokuapp.com/api/v2/'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        item_dict = {}
        equipments = data['data']
        for entry in equipments:
            inStock = item_dict[equipments] = {
                'name': entry['name'],
                'quantity': entry['id'],
                'description': entry['description'],
                'image': entry['image']
            }
            return inStock
print(test())