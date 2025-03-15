import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import dotenv_values
getenv = dotenv_values(".env")
json_path=getenv.get('json_path')

# Load your Firebase credentials
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
