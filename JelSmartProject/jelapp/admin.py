from django.contrib import admin
from .models import Kezikonyv, Gyakorlo, Fogalom

@admin.register(Kezikonyv)
class KezikonyvAdmin(admin.ModelAdmin):
    list_display = ('cim', 'kategoria', 'letrehozva')
    search_fields = ('cim', 'leiras')
    list_filter = ('kategoria',)

@admin.register(Gyakorlo)
class GyakorloAdmin(admin.ModelAdmin):
    list_display = ('cim', 'nehezseg', 'letrehozas_datum')
    list_filter = ('nehezseg',)
    search_fields = ('cim', 'leiras')
    ordering = ('-letrehozas_datum',)

@admin.register(Fogalom)
class FogalomAdmin(admin.ModelAdmin):
    list_display = ('nev', 'kategoria', 'letrehozas_datum')
    search_fields = ('nev', 'definicio')