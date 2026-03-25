from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    #return HttpResponse("Hello World. You are currently at the home page.")
    return render(request, 'website/index.html')

def About(request):
    # return HttpResponse("Hello World. You are currently at the about page.")
    return render(request, 'website/about.html')

def Contact(request):
    # return HttpResponse("Hello World. You are currently at the contact page.")
    return render(request, 'website/contact.html')