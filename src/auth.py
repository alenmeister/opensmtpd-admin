"""Routes for user authentication"""

from typing import Optional

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

from . import login_manager
from .forms import LoginForm
from .models import User

auth_blueprint = Blueprint(
    'auth_blueprint', __name__, 
    template_folder='templates',
    static_folder='static'
)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Authenticate an existing user"""

    if current_user.is_authenticated:
        return redirect(url_for('main_blueprint.dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(password=form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main_blueprint.dashboard'))

        flash('Invalid username and password combination', category='warning')
        return redirect(url_for('auth_blueprint.login'))

    return render_template(
        'login.jinja2',
        title='Authentication',
        form=form
    )


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    """
    Verify if user is authenticated upon page load.

    :param user_id:
        Email (user_id) to retrieve from session cookie.
    """
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to login page"""
    flash('To access this page you must be authenticated', category='warning')
    return redirect(url_for('auth_blueprint.login'))
