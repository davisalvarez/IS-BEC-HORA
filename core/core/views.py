from django.shortcuts import render

# Create your views here.

def Sigin(request):
    return render(request, 'sign_In.html')


def home(request):
    return render(request, 'home.html')