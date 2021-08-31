from django.contrib import admin

# Register your models here.
from app.models import Stu

# admin.site.register(Stu)
@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    
    list_display=('id','name','age','sex','classid')

    list_display_links=('id','name')

    list_per_page = 10

    ordering = ('id',)

    # list_editable = ['age','sex','classid']