from django.contrib import admin
from .models import Agent, Property, BlogPost, BlogCategory

admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
