import firebase_admin
from firebase_admin import credentials, firestore

# Load your Firebase credentials
cred = credentials.Certificate("json\\vardano-contact-section-firebase-adminsdk-fbsvc-748ca56294.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
