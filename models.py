from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.model):
    """Product in the system"""
    __tablename__ = 'Product'

class Inventory(db.model):
    """Inventory in the system"""
    __tablename___ = 'inventory'

class Customer(db.model):
    """User in the system"""
    __tablename__ = 'customer'


def connect_db(app):
    """Connect this database to Flask"""


    db.app = app
    db.init_app(app)
