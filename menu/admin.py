from django.contrib import admin
from .models import Prato
from django.contrib.admin.options import ModelAdmin, TabularInline

# Register your models here.
class PratoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'ingredientes', 'preparo', 'pessoas','tempodepreparo')
	search_fields = ('nome',)
	ordering = ('nome',)

admin.site.register(Prato, PratoAdmin)