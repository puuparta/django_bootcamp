from django.contrib import admin
from article.models import Article

#enabloidaan auto admin
admin.site.register(Article)