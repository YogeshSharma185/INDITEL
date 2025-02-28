# my_app/admin.py

from django.contrib import admin
from .models import wifi, Contact, postpaid, prepaid, dth

# Register your custom models
admin.site.register(wifi)
admin.site.register(Contact)
admin.site.register(postpaid)
admin.site.register(prepaid)
admin.site.register(dth)
