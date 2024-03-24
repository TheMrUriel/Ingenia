from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Usuario)
class CompradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'correo')
    search_fields = ('usuario__username', 'correo')
