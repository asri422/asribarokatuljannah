from django.shortcuts import render

def index(request):
    return render(request, 'asri/index.html')

def penmu(request):
    return render(request, 'asri/penmu.html')

def opini(request):
    return render(request, 'asri/opini.html')

def puisi(request):
    return render(request, 'asri/puisi.html')

def aboutme(request):
    return render(request, 'asri/aboutme.html')

