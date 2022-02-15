from dataclasses import field
import imp
from django.contrib import admin

from .models import Tehtava, Kategoria

# 1
# admin.site.register(Tehtava)

# 2
@admin.register(Tehtava)
class TehtavaAdmin(admin.ModelAdmin):
    list_display = ["id", "otsikko", "kategoria"]


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    # list_display = ["nimi"]
    pass

