from django.contrib import admin
from .models import Event, ContactUs, EventGalery, EventOrganizer, Sponsor, EventCategory
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    search_fields = ['tittle','description']
    list_display = ('tittle','event_date','place','is_active','created_at',)

class ContactUsAdmin(admin.ModelAdmin):
    search_fields = ['name','email']
    list_display = ('name','email','subject','created_add',)

admin.site.register(Event,EventAdmin)
admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(EventGalery)
admin.site.register(EventOrganizer)
admin.site.register(Sponsor)
admin.site.register(EventCategory)