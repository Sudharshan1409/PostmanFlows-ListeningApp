from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class RedirectUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dropboxUrl = db.Column(db.String(255), nullable=False)

