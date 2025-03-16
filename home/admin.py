from django.contrib import admin

from .models import member,travel,Bmenu,Dmenu,Join,breakfast,Dinner

# Register your models here.

admin.site.register(member)
admin.site.register(travel)
admin.site.register(Bmenu)
admin.site.register(Dmenu)
admin.site.register(Join)
admin.site.register(breakfast)
admin.site.register(Dinner)