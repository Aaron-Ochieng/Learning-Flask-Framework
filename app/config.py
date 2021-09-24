import os


class Configuration():
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SECRET_KEY = 'This is a secret key'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = False
