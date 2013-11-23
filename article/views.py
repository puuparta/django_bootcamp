from django.shortcuts import render
from django.shortcuts import render_to_response

# session requires HttpResponse
from django.http import HttpResponse
from article.models import Article
#from django.template.loader import get_template
#from django.template import Context

def hello(request):
   name=request.GET["k"]
   html="Moro %s. Mita kuuluu?" % name
   return render_to_response('hello.html',{'name':html})

def articles(request):
	language = "en-gb"
	session_language = "en-gb"
	if 'lang' in request.COOKIES:
		language = request.COOKIES["lang"]


	if 'lang' in request.session:
		session_language = request.session["lang"]

	return render_to_response('articles.html',
								{'articles': Article.objects.all(),
								  'language': language,
								  'session_language': session_language})

def article(request, article_id=1):
	return render_to_response('article.html',
								{'article' : Article.objects.get(id=article_id)})

def language(request,language="en-gb"):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie("lang", language)
	request.session["lang"] = language
	return response



