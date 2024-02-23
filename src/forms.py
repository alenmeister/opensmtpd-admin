"""Custom forms and validators"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp


class LoginForm(FlaskForm):
    """Authentication form"""

    email = StringField(
        'Email address',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email address')
        ]
    )

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Go')


class UpdateForm(FlaskForm):
    """Update credentials form"""

    old_password = PasswordField('Old password', validators=[DataRequired()])

    new_password = PasswordField(
        'New password',
        validators=[
            DataRequired(),
            Length(min=12, message='Password must be 12 characters or longer'),
            #Regexp(
            #    '(?=[A-Za-z0-9@#$%^&+!=]+$)^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$',
            #    message='Password must contain at least one uppercase, one lowercase and one number'
            #)
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )
