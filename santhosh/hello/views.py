from django.shortcuts import render 
from django.http import HttpResponse

def hi(request):
   # return HttpResponse("Hello, Django!")
   return render(request,'hello/home.html')