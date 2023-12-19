from django.contrib import admin
from . import models
from .models import formresponse
# Register your models here.
@admin.register(formresponse)
class Form_Response(admin.ModelAdmin):
    list_display=[f.name for f in formresponse._meta.get_fields()]
    list_filter=('name','city','country','contact','volas','contact')
    sortable_by=('name','city','contact','volas')