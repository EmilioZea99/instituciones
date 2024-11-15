# instituciones_app/views.py
from django.http import JsonResponse

# Lista de usuarios válidos y su institución asociada
USER_INSTITUTION_MAPPING = {
    "padre-familia-ernesto-1": "Western_Peaks_Elementary",
    "aux-jose-1": "Western_Peaks_Elementary",
    "padre-familia-valentina-1": "Ravenna_High_School",
    "aux-camila-1": "Ravenna_High_School",
}


def get_institution_from_user(request, user_id):
    # Verificar si el usuario está en la lista de usuarios válidos
    if user_id not in USER_INSTITUTION_MAPPING:
        return JsonResponse({"error": "User not recognized"}, status=400)

    # Devolver la institución asociada al usuario
    institution_name = USER_INSTITUTION_MAPPING[user_id]
    return JsonResponse({"institution": institution_name})
