from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','is_active','created_at',)
    resource_class = CategoryResource


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['user']
    list_display = ('user','is_active',)
    resource_class = AuthorResource
    actions = ['logic_delete_autors','logic_activation_autors']

    def logic_delete_autors(self,request,queryset):
        for author in queryset:
            author.is_active = False
            author.save()

    def logic_activation_autors(self,request,queryset):
        for author in queryset:
            author.is_active = True
            author.save()

    def get_actions(self,request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(News)