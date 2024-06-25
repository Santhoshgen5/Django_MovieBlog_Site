from django.contrib import admin
from .models import moviemodel, commentmodel
# Register your models here.

class commentadmin(admin.ModelAdmin):
    list_display = ['username', 'comment', 'movie', 'rating']

admin.site.register(moviemodel)
admin.site.register(commentmodel, commentadmin)