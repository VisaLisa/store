import os
import stripe

from flask import Flask, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from forms import AddProductForm
from models import db, connect_db, Product

app = Flask(__name__)
toolbar = DebugToolbarExtension(app)
app.config['SECRET_KEY'] = "stuffthings"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgres:///lisastore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51IdJOfLr6dKpoHJsWZmDW1ImIVKAreVf0GhQDzfTT74uiNGeR2Pd42ZzFOHIJ4Al1PmZMU54btPNINuFbbsve5SP00ynr27tFh'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51IdJOfLr6dKpoHJs2lQ0qg5DYKkmBSsnPlpiL393r4pN0YKqN0p1dpAf0X0VGJbjSXWjy027R7foLtBJLewEAvjq00M1PmdOqC'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    """Show homepage - show product list"""
    return render_template("index.html", key=stripe_keys['publishable_key'])

# TODO: product page - add, delete, edit
@app.route('/products')
def show_all_products():
    """Return a list of products"""

    product_list = Product.query.all()
    return render_template('products.html', product_list=product_list)

@app.route('/product/add', methods=["GET", "POST"])
def add_product():

    form = AddProductForm()

    # validate product
    if form.validate_on_submit():



# @app.route('/product/<int:product_id>', methods=["GET", "POST"])
# def show_product():
"""product list page - all products"""

# cart - add product to cart 
    # app.route(methods=["GET","POST"])
# checkout session

# @app.route('/pay', methods=['POST'])
# def pay():
    # amount
    # customer information from form
    # currency
    # charge - customer id, amount, currency, description
# order confirmation


