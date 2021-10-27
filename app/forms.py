from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    poke_id = StringField('Search for a Pokemon', validators = [DataRequired()])
    submit = SubmitField('Submit')