# The app directory is constructed as a package and thus has a __init__.py
# file to run whenever the package is imported
# in this case we create the Flask app object and import the routes

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the Flask app object
app = Flask(__name__)

# Set the config for the app
app.config.from_object(Config)

# Setup the database connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import the routes and models source files,
# this will make the database models visible to the Flask application
from app import routes, models

