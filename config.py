import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    UPLOAD_FOLDER = 'webapp/static/images/'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'medifycare24@gmail.com'
    MAIL_PASSWORD = 'mlxc mevq stuk hfoa'
class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # setup mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://medifycare:MedifyCare_2024@localhost/medifycare'
    # MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'medifycare'
    # MYSQL_PASSWORD = 'MedifyCare_2024'
    # MYSQL_DB = 'medifycare'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit image upload
    
