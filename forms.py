from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, Optional, ValidationError
# from models import db, Query_Form, App_Inquiry_form  # Import your model



class sign_in(FlaskForm):
    username = StringField('User name', validators=[DataRequired()]) 
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Login')

