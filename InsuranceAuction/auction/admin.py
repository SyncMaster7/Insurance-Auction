from django.contrib import admin
from .models import Vehicle, Motorcycle, SparePart, Trailer, OtherItem

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Motorcycle)
admin.site.register(Trailer)
admin.site.register(SparePart)
admin.site.register(OtherItem)
