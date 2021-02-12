from django.contrib import admin
from . models import NewJobs
from django.utils.html import format_html
# Register your models here.
class JobAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('SerialNumber', 'company','title', 'location', 'postdate','lastdate','action')
    search_fields = ('company', 'title')
    list_filter = ('location','title')
    list_display_links = ('company','title')
    list_editable= ('action',)

admin.site.register(NewJobs)
