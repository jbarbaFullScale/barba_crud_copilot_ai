from flask import Flask
from extensions import db
from routes import contact_bp
from flask_migrate import Migrate
from models import Contact

import os

app = Flask(__name__)

# Load configuration based on environment
env = os.getenv('FLASK_ENV', 'development')  # Default to 'development'
if env == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Register the blueprint
app.register_blueprint(contact_bp)

if __name__ == "__main__":
    with app.app_context():

        db.create_all()  # Create database tables
    app.run(debug=True)
