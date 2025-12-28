from django.http import JsonResponse

def login_user(request):
    # API PART 
    # Logic for login authentication
    return JsonResponse({"message": "Login API placeholder"})

def register_user(request):
    # API PART 
    # Logic for user registration
    return JsonResponse({"message": "Register API placeholder"})

def user_profile(request):
    # API PART 
    # Logic for fetching/updating user profile
    return JsonResponse({"message": "User profile API placeholder"})
