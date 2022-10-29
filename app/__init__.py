from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import User, db
from flask_login import LoginManager



#need to import blueprints!!!
app =Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)

login.login_view = 'logMeIn'


from . import routes
from . import models