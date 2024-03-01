from functools import wraps

from flask import abort
from flask_login import current_user

from .models import Permission


def admin_required(f):
    """Restrict view to users with administrator permission"""

    @wraps(f)
    def decorated_view(*args, **kwargs):
        if not current_user.has_role(Permission.ADMIN):
            abort(403)
        return f(*args, **kwargs)

    return decorated_view
