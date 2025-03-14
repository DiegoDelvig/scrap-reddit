import firebase_admin
from firebase_admin import db, credentials

def add(element, dir):
	ref = db.reference(f'/{dir}')
	ref.set(element)


def connect():
	cred = credentials.Certificate("credentials.json")
	firebase_admin.initialize_app(cred, {'databaseURL': DATABASEURL})
