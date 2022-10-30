import requests

def test():
    
    url = f'https://botw-compendium.herokuapp.com/api/v2/entry/lizal_bow'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        # item_dict = {}
        # equipments = data['data']['equipment']
        # for entry in equipments:
        dict = {
            'name': data['data']['name'],
            'quantity': data['data']['id'],
            'description': data['data']['description'],
            'image': data['data']['image']
        }
        return dict
print(test())
