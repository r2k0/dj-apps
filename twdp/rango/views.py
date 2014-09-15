from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	# context contains info such as the client's machine details
	# request the context of the request
	context = RequestContext(request)

	# dictionary to pass to the template engine as its context
	context_dict = {'boldmessage': "I am bold font from the context"}
	
	# return rendered response to send to the client
	# render_to_response( template, context_dict, context )
	return render_to_response('rango/index.html',context_dict, context)

def about(request):
	return HttpResponse("About. <a href='/rango/'>Index</a>")
