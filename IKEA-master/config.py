import os

# Configuration options fetched from enviroment variables in .flaskenv
# are set here!

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Note that the the triple /// is correct
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False