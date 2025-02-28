from flask import Flask
from config import Config

# Create the Flask app
app = Flask(__name__)


from routes import *

# Load configuration settings from the Config class
app.config.from_object(Config)



