from django.contrib import admin

from demoapp.models import destinations
from demoapp.models import members

# Register your models here.
admin.site.register(destinations)
admin.site.register(members)