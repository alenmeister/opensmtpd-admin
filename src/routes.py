"""Routes for restricted views"""

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user

from . import db
from .forms import UpdateForm

main_blueprint = Blueprint(
    'main_blueprint', __name__, 
    template_folder='templates',
    static_folder='static'
)


@main_blueprint.route('/', methods=['GET'])
@login_required
def dashboard():
    """Dashboard view"""
    return render_template(
        'dashboard.jinja2', 
        title='Dashboard',
        active_url='dashboard',
        current_user=current_user
    )


@main_blueprint.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """Account view"""

    form = UpdateForm()

    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.hash_password(form.new_password.data)
            db.session.commit()

            flash('Your password has successfully been updated')
            return redirect(url_for('main_blueprint.account'))

        flash('Your original password is invalid')

    return render_template(
        'account.jinja2',
        title='Manage Account',
        active_url='account',
        form=form
    )


@main_blueprint.route('/logout')
@login_required
def logout():
    """Logout the current user and redirect to login"""
    logout_user()
    return redirect(url_for('auth_blueprint.login'))
