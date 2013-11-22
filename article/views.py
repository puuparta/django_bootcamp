from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context

def hello(request):
   name=request.GET["k"]
   html="Moro %s. Mita kuuluu?" % name
   return render_to_response('hello.html',{'name':html})

