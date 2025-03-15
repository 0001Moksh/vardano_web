import firebase_admin
from firebase_admin import credentials, firestore
from django.core.management.base import BaseCommand

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("json/vardano-contact-form-1-firebase-adminsdk-fbsvc-de1e82152a.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

class Command(BaseCommand):
    help = "Fetch contacts from Firebase"

    def handle(self, *args, **kwargs):
        contacts_ref = db.collection("contacts")
        docs = contacts_ref.stream()

        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")
