from django.http import HttpResponse


def home_page(request):
    print("Home Page")
    return HttpResponse("This Is Home Page")