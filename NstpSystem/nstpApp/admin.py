from django.contrib import admin
from .models import registration

admin.site.site_header = "NSTP Admin"
admin.site.site_title = "NSTP Admin Portal"
class UserAdmin(admin.ModelAdmin):
    list_display = []
    
    
admin.site.register(registration, UserAdmin)

# Register your models here.
