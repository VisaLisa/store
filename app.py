from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy


from forms
from models

app = Flask(__name__)
toolbar = DebugToolbarExtension(app)

app.config ['SQLALCHEMY_DATABASE_URI'] = ('postgres:///lisastore')
db = SQLAlchemy(app)
