from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Product)
admin.site.register(models.Fabricator)
admin.site.register(models.Shoes_type)
admin.site.register(models.Sex)
admin.site.register(models.Sizes)
admin.site.register(models.Colors)