from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rango.models import Category

def index(request):
	context = RequestContext(request)
	
	category_list = Category.objects.order_by('id')[:5]
	context_dict = {'categories': category_list }
	
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Index</a>")
