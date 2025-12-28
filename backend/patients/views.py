from django.http import JsonResponse

def patient_vitals(request):
    # API PART 
    return JsonResponse({"message": "Vitals API placeholder"})

def patient_medications(request):
    # API PART 
    return JsonResponse({"message": "Medications API placeholder"})

def patient_alerts(request):
    # API PART
    # Fetch alerts for patient
    return JsonResponse({"message": "Alerts API placeholder"})
