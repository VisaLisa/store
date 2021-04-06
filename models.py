from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """Product in the system"""
    # product id, inventory status, product name, product description, price
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    product_name = db.Column(db.Text, nullable = True)
    product_desc = db.Column(db.Text)
    price = db.Column(db.Integer)
    status = db.Column(db.Boolean, nullable = False, default = True)

# class Customer(db.Model):
#     """Customer in the system"""
#     __tablename__ = 'customer'
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#     name = db.Column(db.String, nullable=False)
#     address = db.Column(db.String, nullable=False)
#     # customer id, customer name, customer address,


# class Order(db.Model):
#      """Order in the system"""
#      # order id, customer id, product id,  number of products, order status
#      __tablename__ = 'orders'
#      id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#      customer_id = 
    

def connect_db(app):
    """Connect this database to Flask"""
    db.app = app
    db.init_app(app)


# TODO: build the schema, field and table
# TODO: break it out down from backend to front end; connect api; then client side
# README - uses Stripe API (payment)
# bootstrap - make it decent and showcase to someone, 