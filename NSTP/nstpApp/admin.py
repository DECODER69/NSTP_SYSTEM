from django.contrib import admin
from .models import  registration, certifications, platoons

# Register your models here.

admin.site.register(registration)
admin.site.register(certifications)
admin.site.register(platoons)
# admin.site.register(CustomUser)

