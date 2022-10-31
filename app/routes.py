
from app import app
import json
import requests
from flask import Blueprint, render_template, request, redirect, url_for,flash
from flask_login import login_required, login_user, logout_user, current_user
from app.forms import UserCreationForm, UserLoginForm, ItemForm  #modified import. checked for functionality? y/n< >evan
from .models import Product, User, db #recently added imports. checked for functionality? y/n< >evan
from werkzeug.security import check_password_hash #recently added import. checked for functionality? y/n< >evan


#testing to add to git

@app.route('/')
def homePage():
    return render_template('index.html')

#recently added items route. checked for functionality? y/n< >evan
@app.route('/wares', methods=["GET"]) 
def wares():
    
    items = Product.query.all()
    
    return render_template('wares.html', items=items)
    


#recently added items route. checked for functionality? y/n< >evan
@app.route('/items', methods=["GET","POST"]) 
def items():
    form = ItemForm()
    dict = {}
    # print('front-front')
    if request.method == "POST":
        # print('front')
        if form.validate():
            item = form.item.data
            url = f'https://botw-compendium.herokuapp.com/api/v2/entry/{item}'
            response = requests.get(url)
            if response.ok:
                data = response.json()
                # item_dict = {}
                # equipments = data['data']['equipment']
                # for entry in equipments:
                dict[item.title()] = {
                    'name': data['data']['name'],
                    'quantity': data['data']['id'],
                    'image': data['data']['image'],
                    'description': data['data']['description']
                }
                name = dict[item.title()]['name']
                quantity = dict[item.title()]['quantity']
                img_url = dict[item.title()]['image']
                description = dict[item.title()]['description']
                
                
                item = Product.query.filter_by(item=item).first()
                if item:
                    pass
                else:
                    item = Product(name, quantity, img_url, description)

                    db.session.add(item)
                    db.session.commit()
                dict['id'] = item.id
                return render_template('items.html', x=form, item=item)
    return render_template('items.html', x=form)


#recently added cart route. checked for functionality? y/n< >evan
@app.route('/cart')
@login_required
def cart():
    # item = current_user.add_2_cart.all()
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
    return render_template('signup.html', s=form)


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

    return render_template('login.html', l=form)

@app.route('/logout')
def logMeOut():
    flash('Thank you for shopping with us!', 'secondary')
    logout_user()
    return render_template('index.html')