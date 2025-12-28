from django.http import HttpResponse

def chat_history(request):
    # API PART
    return HttpResponse("Chat works")

def call_logs(request):
    # API PART
    return HttpResponse("Calls works")


