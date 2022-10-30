#recently added whole page. checked for functionality? y/n< >
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime

db = SQLAlchemy()

cart = db.Table('cart',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime,nullable=False, default=datetime.utcnow())
    add_2_cart = db.relationship("Product",
        secondary = cart,
        backref = db.backref('Shopper', lazy='dynamic'),
        lazy = 'dynamic'
    )

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def add2cart(self, item):
        self.cartAdd.append(item)
        db.session.commit()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50), nullable=False, unique=True)
    # price = db.Column(db.Numeric(8,2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(5000), nullable=False)

    def __init__(self, id, item, quantity, img_url, description):
        self.id = id
        self.item = item
        # self.price = price
        self.quantity = quantity
        self.img_url = img_url
        self.description = description