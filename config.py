class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vadim:1@localhost:5432/test1'
    SECRET_KEY = 'something secret'

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_SALT = 'bcrypt'