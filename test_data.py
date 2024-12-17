import logging
import random
from webapp import create_app
from webapp import db
from webapp.auth.models import User, Role
from webapp.auth import bcrypt
from config import ProdConfig


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

log = logging.getLogger(__name__)
app = create_app(ProdConfig)
app.app_context().push()



fake_users = [
    {'username': 'Esra', 'role': 'patient', 'activetion': 1},
    {'username': 'Dr.James Smith', 'role': 'doctor', 'specialty': 'cardiology', 'bio': '15 years of experience in diagnosing and treating heart conditions.', 'activetion': 1},
    {'username': 'Dr.Susan Martin', 'role': 'doctor', 'specialty': 'neurology', 'bio': '5 years of experiance in neurologist with a focus on neurodegenerative diseases and stroke management.'},
    {'username': 'Dr.Michael Johnson', 'role': 'doctor', 'specialty': 'orthopedics', 'bio': '7 years of experinace in orthopedic surgeon specializing in sports injuries and joint replacement.'},
    {'username': 'Dr.Emily Clark', 'role': 'doctor', 'specialty': 'pediatrics', 'bio': '10 years expertise in child development and preventive care.focusing on early diagnosis and management of common pediatric conditions.'}
]
fake_roles = ['doctor', 'patient']


def generate_roles():
    roles = list()
    for rolename in fake_roles:
        role = Role.query.filter_by(name=rolename).first()
        if role:
            roles.append(role)
            continue
        role = Role(rolename)
        roles.append(role)
        db.session.add(role)
        try:
            db.session.commit()
        except Exception as e:
            log.error("Erro inserting role: %s, %s" % (str(role),e))
            db.session.rollback()
    return roles

def generate_users():
    users = list()
    for item in fake_users:
        user = User.query.filter_by(username=item['username']).first()
        if user:
            users.append(user)
            continue
        user = User()
        poster = Role.query.filter_by(name=item['role']).one()
        user.roles.append(poster)
        user.username = item['username']
        if item['role'] == 'doctor':
            user.specialty = item['specialty']
            user.bio = item['bio']
        user.password = bcrypt.generate_password_hash("password")
        users.append(user)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            log.error("Eror inserting user: %s, %s" % (str(user), e))
            db.session.rollback()
    return users


generate_roles()
generate_users()
