from django.contrib import admin

# Register your models here.

from.models import Art, Artist, Period

admin.site.register(Art)
admin.site.register(Artist)
admin.site.register(Period)
