from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import box,suggestion

admin.site.register(box)
admin.site.register(suggestion)