from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length, URL, Optional

class AddProductForm(FlaskForm):
    product_name = StringField(
        "Product name",
        validators=[InputRequired()],
    )
    product_desc = TextAreaField(
        "Product description",
        validators=[Optional(), Length(min=10)]
    )
    price = IntegerField(
        "price",
        validators=[InputRequired()]
    )
    status = BooleanField(
        "Avaliable"
    )

# EditProductForm()