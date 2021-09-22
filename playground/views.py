from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request => response
#request handler
#action

def say_hello(request):
    return HttpResponse("Hello World")

def send_html(request):
    return render(request, "hello.html")

def send_html_data(request):
    x = 1
    x = 2
    return render(request, "data.html", {"name": "Ben"})

