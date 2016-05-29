from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
	return HttpResponse("Rango says hey there partner! <br/> <br/> Hello world! <br/> <br/> <a href='/rango/about1'>About</a>")

def about1(request):
	return HttpResponse("Rango says here is the about page. <br/> <br/> <a href=' /rango/'>Index </a>")
