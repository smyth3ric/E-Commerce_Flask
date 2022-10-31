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
# @app.route('/items', methods=["GET","POST"])
# def items():
#     form = ItemForm()
#     dict = {}
#     print('front-front')
#     if request.method == "POST":
#         print('front')
#         if form.validate():
#             item = form.item.data
#             url = f'https://botw-compendium.herokuapp.com/api/v2/entry/{item}'
#             response = requests.get(url)
#             if response.ok:
#                 data = response.json()
#                 # item_dict = {}
#                 # equipments = data['data']['equipment']
#                 # for entry in equipments:
#                 dict[item.title()] = {
#                     'name': data['data']['name'],
#                     'quantity': data['data']['id'],
#                     'image': data['data']['image'],
#                     'description': data['data']['description']
#                 }
#                 name = dict[item.title()]['name']
#                 quantity = dict[item.title()]['quantity']
#                 img_url = dict[item.title()]['image']
#                 description = dict[item.title()]['description']
#             item = Product.query.filter_by(item=item).first()
#             if item:
#                 pass
#             else:
#                 item = Product(name, quantity, img_url, description)
#                 db.session.add(item)
#                 db.session.commit()
#             return render_template('items.html', form=form, item=item)
#     return render_template('items.html', form=form)