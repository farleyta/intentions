from django.http import HttpResponse


def api(request):
    return HttpResponse("Hello, world")
