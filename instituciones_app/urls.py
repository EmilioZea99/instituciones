# instituciones_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path(
        "institution/<str:user_id>/",
        views.get_institution_from_user,
        name="get_institution_from_user",
    ),
]
