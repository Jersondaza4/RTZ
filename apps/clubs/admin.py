from django.contrib import admin

# Register your models here.
from .models import CarBrand, Club
# Register your models here.

class ClubAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_display = ('name','car_brand','created_at',)

class CarBrandAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name',)

admin.site.register(Club,ClubAdmin,)
admin.site.register(CarBrand,CarBrandAdmin)