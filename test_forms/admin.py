from django.contrib import admin

from . import models

admin.site.register(models.CustomerAddress)
admin.site.register(models.Inspection)
admin.site.register(models.Section1)
admin.site.register(models.Section2)
