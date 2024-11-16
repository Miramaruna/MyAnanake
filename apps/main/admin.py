from django.contrib import admin
from .models import Personal, Home
# Register your models here.

@admin.register(Personal)
class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'photo', 'github', 'google', 'twitter', 'facebook']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    fields = ['github', 'twitter', 'facebook', 'google']