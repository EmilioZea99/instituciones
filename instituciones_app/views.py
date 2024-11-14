# instituciones_app/views.py
from django.http import JsonResponse


def get_institution_from_user(request, user_id):
    try:
        # Extraer el nombre de la institución después del guion "-"
        institution_name = user_id.split("-", 1)[1]
        return JsonResponse({"institution": institution_name})
    except IndexError:
        return JsonResponse({"error": "Invalid user_id format"}, status=400)
