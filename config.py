import os

class Config:
    """Base configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///contacts.db'  # App database


class TestingConfig(Config):
    """Testing configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///:memory:')  # Use in-memory database for tests
    TESTING = True