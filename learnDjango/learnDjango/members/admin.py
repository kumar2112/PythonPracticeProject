
from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display  = ("firstname", "lastname")
    search_fields = ("firstname","lastname")
    ordering = ("firstname",)
    
# Register your models here.
admin.site.register(Member,MemberAdmin)