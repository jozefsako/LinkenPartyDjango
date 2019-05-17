from django.contrib import admin
from .models import AUsers, Events, Participations

# Register your models here.

admin.site.register(Events)
admin.site.register(AUsers)
admin.site.register(Participations)
