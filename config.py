import os

class Config:
    # Generates a random secure key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-this-in-prod'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///gymstore.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False