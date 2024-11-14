# instituciones_app/views.py
from django.http import JsonResponse

# Lista de instituciones válidas
VALID_INSTITUTIONS = [
    "GORDON_BERNELL_CHARTER",
    "CROWLEY_COUNTY_ELEMENTARY_K-6",
    "KENNEDALE_H_S",
    "Ravenna_High_School",
    "BALDWIN_ELEM",
    "Sunrise_Elementary",
    "CORNING_PAINTED_POST_MIDDLE_SCHOOL",
    "FOX_HOLLOW_ELEMENTARY_SCHOOL",
    "Central_Elementary_School",
    "Camden_High",
    "Anson_Co_Early_College_High",
    "Lockland_Middle_School",
    "OVERBROOK_ELEMENTARY_SCHOOL",
    "WARREN_CENTRAL_INTERMEDIATE",
    "Western_Peaks_Elementary",
    "Fayette_Elementary_School",
]


def get_institution_from_user(request, user_id):
    try:
        # Extraer el nombre de la institución después del guion "-"
        parts = user_id.split("-", 1)
        if len(parts) < 2:
            raise ValueError("Invalid user_id format")

        institution_name = parts[1]

        # Verificar si la institución está en la lista de instituciones válidas
        if institution_name in VALID_INSTITUTIONS:
            return JsonResponse({"institution": institution_name})
        else:
            return JsonResponse({"error": "Institution not recognized"}, status=400)
    except ValueError:
        return JsonResponse({"error": "Invalid user_id format"}, status=400)
