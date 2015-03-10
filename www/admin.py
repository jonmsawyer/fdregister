from django.contrib import admin
from www.models import Event, Registrant

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)

class RegistrantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Registrant, RegistrantAdmin)
