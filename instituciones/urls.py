# instituciones/urls.py
from django.urls import include, path

urlpatterns = [
    path("instituciones/", include("instituciones_app.urls")),
]
