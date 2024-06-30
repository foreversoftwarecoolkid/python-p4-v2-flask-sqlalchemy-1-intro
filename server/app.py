# server/app.py

from flask import Flask
from flask_migrate import Migrate

from models import db  # Import the SQLAlchemy db instance from models

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# Initialize the Flask application to use the database
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
