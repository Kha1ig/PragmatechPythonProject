from django.contrib import admin

from phone.models import ( 
        phone,
        company,
        phoneimei,
        )

# Register your models here.

@admin.register(phone)

class PhoneAdmin(admin.ModelAdmin):
        list_display = ('name', 'brand', 'image', 'price',)
        empty_value_display = 'no data'
        list_display_links = ('name', 'brand',)
        search_fields =('name', 'price',)
        search_help_text = ('find by name and price')
        list_filter = ('brand',)

@admin.register(company)

class CompanyAdmin(admin.ModelAdmin):
        list_display = ('owner', 'bio', )


@admin.register(phoneimei)

class PhoneimeiAdmin(admin.ModelAdmin):
        list_display = ('imei', 'reseption_date',)

        #@admin.display(description='phones')
        


# admin.site.register(phone)
# admin.site.register(company)
# admin.site.register(phoneimei)


