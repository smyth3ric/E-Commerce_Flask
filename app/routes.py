
from app import app
import requests
from flask import Blueprint, render_template, request, redirect, url_for,flash
from flask_login import login_required, login_user, logout_user, current_user
from app.forms import UserCreationForm, UserLoginForm, ItemForm  #modified import. checked for functionality? y/n< >evan
from .models import Product, User, db #recently added imports. checked for functionality? y/n< >evan
from werkzeug.security import check_password_hash #recently added import. checked for functionality? y/n< >evan




@app.route('/')
def homePage():
    return render_template('index.html')

#recently added items route. checked for functionality? y/n< >evan
@app.route('/search') 
def search():
    return render_template('search.html')
    


#recently added items route. checked for functionality? y/n< >evan
@app.route('/items', methods=["GET","POST"]) 
def items():
    form = ItemForm()
    dict = {}
    print('front-front')
    if request.method == "POST":
        print('front')
        if form.validate():
            item = form.item.data
            url = f'https://botw-compendium.herokuapp.com/api/v2/entry/{item}'
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
            item = Product.query.filter_by(item=dict['name']).first()
            if item:
                pass
            else:
                item = Product(dict['name'], dict['quantity'],dict['image'],dict['description'])

                db.session.add(item)
                db.session.commit()
            dict['id'] = item.id
            return render_template('items.html', x=form, item=dict)
    return render_template('items.html', x=form, item=dict)


#recently added cart route. checked for functionality? y/n< >evan
@app.route('/cart')
@login_required
def cart():
    # item = current_user.cartAdd.all()
    return render_template('cart.html')


@app.route('/signup', methods=["GET", "POST"])
def signMeup():
    form= UserCreationForm()
    if request.method == "POST":
        if form.validate():#recently added signUp function. checked for functionality? y/n< >evan
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data

            #add user to database
            user = User(username, first_name, last_name, email, password)
            
            #add instance to SQL
            user.saveToDB()

            flash('Shopper registered!', 'success')

            return render_template('login.html')#checked y/n <> evan
        else:
            flash('You are not valid. Please try once more.')  
    return render_template('signup.html', form=form)


 #recently added login function. checked for functionality? y/n< >evan
@app.route('/login', methods = ["GET", "POST"])
def logMeIn():
    form= UserLoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password= form.password.data

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    flash('Incorrect Password!', 'danger')
            else:
                flash('User does not exist!', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logMeOut():
    flash('Thank you for shopping with us!', 'secondary')
    logout_user()
    return render_template('index.html')