from django.shortcuts import render

def home(request):
     return render(request, 'blog/home.html', {'message': 'This is dynamic data from Django!'})
 
def about(request):
     return render(request, 'blog/home.html', {'message': 'This is the about page'})
     
     
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
