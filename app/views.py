from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase_admin import firestore
from django.shortcuts import render
from dotenv import dotenv_values
getenv = dotenv_values(".env")
recivers_mail=getenv.get('recivers_mail')

def home(request):
    return render(request, 'index.html')

# Initialize Firestore
db = firestore.client()

@csrf_exempt
def save_contact(request):
    if request.method == "POST":
        try:
            # Parse JSON data
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            message = data.get("message")

            if not name or not email or not message:
                return JsonResponse({"error": "All fields are required."}, status=400)

            # Save data to Firestore
            contact_ref = db.collection("contacts").document()
            contact_ref.set({"name": name, "email": email, "message": message})

            # Send an email notification
            subject = f"Vardano Books web - New Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_email = recivers_mail
            
            send_mail(
                subject,
                body,
                email,  # From email
                [recipient_email],  # To email
                fail_silently=False,
            )

            return JsonResponse({"success": True, "message": "Contact saved and email sent successfully!"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
