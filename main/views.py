from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")


def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def dz311(request):
    return render(request, "dz311.html")

def dz312(request):
    return render(request, "dz312.html")

def dz313(request):
    return render(request, "dz313.html")




