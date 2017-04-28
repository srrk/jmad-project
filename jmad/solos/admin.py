from django.contrib import admin
from .models import Solo

# Register your models here.
class SoloAdmin(admin.ModelAdmin):
    model = Solo
    list_display = ['track', 'artist', 'get_duration']

admin.site.register(Solo, SoloAdmin)
