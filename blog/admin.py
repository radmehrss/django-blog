from django.contrib import admin
from blog.models import POST,category,Comment
from django_summernote.admin import SummernoteModelAdmin

class postadmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title","status","login_require","author","counted_view","published_date","created_date")
    list_filter = ("status","author")
    search_fields = ["title","content"]
    summernote_fields = ('content')

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("name","status","post","approved","created_date")
    list_filter = ("approved","post")
    search_fields = ["name","post"]

admin.site.register(category)
admin.site.register(POST,postadmin)
admin.site.register(Comment)