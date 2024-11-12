from sqlalchemy_serializer import SerializerMixin
from models.extensions import db


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-reports',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # One-to-many relationship with IncidentReport using back-populate
    reports = db.relationship('IncidentReport', back_populates='user', lazy=True)