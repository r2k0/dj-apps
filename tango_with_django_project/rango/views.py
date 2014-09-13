from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	#return HttpResponse("hello from Rango <a href='/rango/about'>About</a>")
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Index</a>")
