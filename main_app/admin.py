from django.contrib import admin
from .models import register_table
from .models import contact

# Register your models here.
admin.site.register(contact)
admin.site.register(register_table)



