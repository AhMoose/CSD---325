from django.http import HttpResponse

def home(request):
    return HttpResponse("Hernandez says Hello!")