
from django.shortcuts import render, HttpResponse

# Create your views here.

def index( request):
  return render(request, 'ikkuuu/login.html')



def list(request):
  return render(request, 'ikkuuu/list.html')
