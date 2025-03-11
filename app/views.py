from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase_admin import firestore
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


db = firestore.client()

@csrf_exempt
def save_contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # Save data to Firestore
        contact_ref = db.collection("contacts").document()
        contact_ref.set({"name": name, "email": email, "message": message})

        return JsonResponse({"success": True, "message": "Contact saved successfully!"})

    return JsonResponse({"error": "Invalid request"}, status=400)
