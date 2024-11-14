# instituciones_app/views.py
from django.http import JsonResponse

# Lista de instituciones válidas
VALID_INSTITUTIONS = ["GORDON_BERNELL_CHARTER", "CROWLEY_COUNTY_ELEMENTARY_K-6"]

# Lista de usuarios válidos y su institución asociada
USER_INSTITUTION_MAPPING = {
    "pedro20": "GORDON_BERNELL_CHARTER",
    "emilioZea1": "CROWLEY_COUNTY_ELEMENTARY_K-6",
}


def get_institution_from_user(request, user_id):
    try:
        # Dividir el identificador del usuario en dos partes (usuario e institución)
        parts = user_id.split("-", 1)
        if len(parts) < 2:
            raise ValueError("Invalid user_id format")

        user_name = parts[0]
        institution_name = parts[1]

        # Verificar si el usuario está en la lista de usuarios válidos
        if user_name not in USER_INSTITUTION_MAPPING:
            return JsonResponse({"error": "User not recognized"}, status=400)

        # Verificar si la institución está en la lista de instituciones válidas
        if institution_name not in VALID_INSTITUTIONS:
            return JsonResponse({"error": "Institution not recognized"}, status=400)

        # Verificar si el usuario está asociado a la institución correcta
        if USER_INSTITUTION_MAPPING[user_name] != institution_name:
            return JsonResponse(
                {"error": "User and institution do not match"}, status=400
            )

        # Si el usuario y la institución son válidos y están asociados, devolver la institución
        return JsonResponse({"institution": institution_name})

    except ValueError:
        return JsonResponse({"error": "Invalid user_id format"}, status=400)
