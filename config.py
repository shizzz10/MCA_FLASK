import os

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
    ADMIN_PASSWORD = os.getenv('FLASK_ADMIN_PASSWORD', 'admin')
    ADMIN_USERNAME = os.getenv('FLASK_ADMIN_USERNAME', 'admin')
    
