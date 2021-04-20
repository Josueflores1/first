#from django.http import HttpResponse
#shows the page

from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/index.html')

# Create your views here.
