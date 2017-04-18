# Import the db and app variables from app.py
from app import db, app

# Identify current app
with app.app_context():
	db.create_all()
