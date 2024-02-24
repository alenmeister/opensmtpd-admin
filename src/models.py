"""Database models"""

from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import bcrypt, db


class User(UserMixin, db.Model):
    """User model"""

    __tablename__ = 'credentials'

    email: Mapped[str] = mapped_column(String(255), primary_key=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    domain: Mapped[str] = mapped_column(String(255), nullable=False)


    def hash_password(self, password):
        """Create hashed password"""
        self.password = bcrypt.generate_password_hash(password)


    def verify_password(self, password):
        """Verify hashed password"""
        return bcrypt.check_password_hash(self.password, password)


    def get_id(self):
        """Return the email address to satisfy requirements from Flask-Login"""
        return self.email


    def __repr__(self):
        return f'<User {self.email}>'
