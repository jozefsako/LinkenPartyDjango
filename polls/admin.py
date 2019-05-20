from django.contrib import admin
from .models import AUsers, Events, Participations, AUsersWithouID

# Register your models here.

admin.site.register(Events)
admin.site.register(AUsers)
admin.site.register(Participations)
admin.site.register(AUsersWithouID)
