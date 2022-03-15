from django.contrib import admin

from phone.models import ( 
        phone,
        company,
        )

# Register your models here.

admin.site.register(phone)
admin.site.register(company)