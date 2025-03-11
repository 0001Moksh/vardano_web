from django.urls import path
from . import views
from .views import save_contact

urlpatterns = [
    path('', views.home, name='home'),
    path("save-contact/", save_contact, name="save_contact"),
]