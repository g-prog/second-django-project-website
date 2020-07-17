from django.contrib import admin
from . models import News,Sportsnews,Registrationdata,loginn,home_news


# Register your models here.
admin.site.register(News)
admin.site.register(Sportsnews)
admin.site.register(Registrationdata)
admin.site.register(loginn)
admin.site.register(home_news)

