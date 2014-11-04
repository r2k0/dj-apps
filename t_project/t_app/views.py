from django.template import Context, loader
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<html><body>Test, App</body></html>')

def about(request):
    return HttpResponse("Here is the About Page. <a href='/'>Home</a>")

def better(request):
    t = loader.get_template('better.html')
    c = Context({'current_time': datetime.now(),})
    return HttpResponse(t.render(c))
