from . import bcrypt, AnonymousUserMixin
from .. import db
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from flask import current_app
import hashlib
import uuid

# the junction table for many-many relationship between (user, role)
roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

# the User model
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, index=True, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255))
    specialty = db.Column(db.String(255))
    activetion = db.Column(db.Boolean, default=False)
    bio = db.Column(db.String(255))
    image_filename = db.Column(db.String(150))
    confirmed_at = db.Column(db.DateTime())
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy=True)
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy=True)
    roles = db.relationship(
        'Role',
        secondary=roles,
        backref=db.backref('users', lazy='dynamic')
    )

    def __init__(self, username=""):
        # you first you make manual defalut role then
        self.username = username

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def has_role(self, name):
        for role in self.roles:
            if role.name == name:
                return True
        return False

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return str(self.id)

    def activate(self):
        self.activetion = True
    @property
    def actived_subscription(self):
        return self.activetion

    def generate_reset_password_token(self):
        salt = bcrypt.generate_password_hash(uuid.uuid4().hex).decode('utf-8')
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(self.email, salt=salt)

    @staticmethod
    def validate_reset_password_token(token, user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        try:
             token_user_email = serializer.loads(
                token,
                max_age=current_app.config['RSET_PASS_TOKEN_MAX_AGE'])
        except (BadSignature, SignatureExpired):
            return None
        if token_user_email != user.email:
            return None

        return user

 
# the Role model
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role {}>'.format(self.name)
