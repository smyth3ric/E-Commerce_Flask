
from app import app
from flask import Blueprint, render_template, request, redirect, url_for,flash
from flask_login import login_user, logout_user, current_user
from app.forms import UserCreationForm
from app.forms import UserLoginForm
from .models import User #recently added whole page. checked for functionality? y/n< >evan
from werkzeug.security import check_password_hash #recently added whole page. checked for functionality? y/n< >evan





@app.route('/') 
def homePage():
    return render_template('index.html')



@app.route('/test') 
def test():
    return render_template('test.html')


@app.route('/signup', methods=["GET", "POST"])
def signMeup():
    form= UserCreationForm()
    if request.method == "POST":
        if form.validate():#recently added whole page. checked for functionality? y/n< >evan
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

            return redirect(url_for('auth.logMeIn'))#checked y/n <> evan
        else:
            flash('You are not valid. Please try once more.')  
    return render_template('signup.html', form=form)



@app.route('/login', methods = ["GET", "POST"])
def logMeIn():
    form= UserLoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password= form.password.data

            # print(username, password)

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    # print('Sucessfully logged in')
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    flash('Incorrect Password!', 'danger')
            else:
                flash('User does not exist!', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))