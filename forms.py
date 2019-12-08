from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from Waitlist.models import Restaurant

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class RegistrationForm(FlaskForm):
    company_name = StringField('company_name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        resturant = Restaurant.query.filter_by(username=username.data).first()
        if resturant is not None:
            raise ValidationError('Please use a different username.')
    
        def validate_password(self, password):
            resturant = Restaurant.query.filter_by(password=password.data).first()
            if resturant is not None:
                raise ValidationError('Please use a different password.')