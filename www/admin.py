from django.contrib import admin
from www.models import Event, Registrant

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title', 'from_time', 'to_time', 'description', 'price', 'location', 'is_closed')
admin.site.register(Event, EventAdmin)

class RegistrantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Registrant, RegistrantAdmin)
