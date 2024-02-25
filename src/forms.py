"""Custom forms and validators"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


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

    current_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField(
        'New password',
        validators=[
            DataRequired(),
            Length(min=10, message='Password must be 10 characters or longer'),
            EqualTo('confirm_password', message='Passwords must match')
        ]
    )

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Update password')
