from flask_wtf import FlaskForm
from wtforms.fields import (
     StringField, SelectField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired

# from map.map import map  # ImportError: attempted relative import with no known parent package - just c/p for now
map = {
    "Seattle": {"San Francisco"},
    "San Francisco": {"Seattle", "Los Angeles", "Denver"},
    "Los Angeles": {"San Francisco", "Phoenix"},
    "Phoenix": {"Los Angeles", "Denver"},
    "Denver": {"Phoenix", "San Francisco", "Houston", "Kansas City"},
    "Kansas City": {"Denver", "Houston", "Chicago", "Nashville"},
    "Houston": {"Kansas City", "Denver"},
    "Chicago": {"Kansas City", "New York"},
    "Nashville": {"Kansas City", "Houston", "Miami"},
    "New York": {"Chicago", "Washington D.C."},
    "Washington D.C.": {"Chicago", "Nashville", "Miami"},
    "Miami": {"Washington D.C.", "Houston", "Nashville"}
}

# print(map)
places = [(key, key) for key in map.keys()]
# print(places)

class ShippingForm(FlaskForm):
	sender = StringField('Sender', validators=[DataRequired()])
	recipient = StringField('Recipient', validators=[DataRequired()])
	origin = SelectField('Origin', choices=places)
	destination = SelectField('Destination', choices=places)
	express_shipping = BooleanField('Express Shipping?')
	submit_button = SubmitField('Submit')