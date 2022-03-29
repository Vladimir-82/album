from django.contrib import admin
from .models import App

@admin.register(App)
class PostAdmin(admin.ModelAdmin):
    pass

