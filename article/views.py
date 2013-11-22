from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from article.models import Article
#from django.template.loader import get_template
#from django.template import Context

def hello(request):
   name=request.GET["k"]
   html="Moro %s. Mita kuuluu?" % name
   return render_to_response('hello.html',{'name':html})

def articles(request):
	return render_to_response('articles.html',
								{'articles': Article.objects.all()})

def article(request, article_id=1):
	return render_to_response('article.html',
								{'article' : Article.objects.get(id=article_id)})



