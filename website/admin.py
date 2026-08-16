from django.contrib import admin
from website.models import contact,NewsLetter

# Register your models here.
class contactadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ("name","subject","created_date")
    list_filter = ("email",)
    search_fields = ["subject","message"]
admin.site.register(contact,contactadmin)
admin.site.register(NewsLetter)