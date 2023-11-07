from django.shortcuts import render

def index(request):
    return render(request, 'asri/index.html')

def penmu(request):
    return render(request, 'asri/penmu.html')
