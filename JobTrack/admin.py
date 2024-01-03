from django.contrib import admin

# Register your models here.

from .models import *
from django.utils.translation import gettext_lazy as _

admin.site.register(Job)
admin.site.register(Person)