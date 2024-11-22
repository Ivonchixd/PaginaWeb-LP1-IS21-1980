from django.contrib import admin
from .models import products 

# Register your models here.
#admin.site.register(productos)

class productosAdmin(admin.ModelAdmin):
    list_display = ('codigoProducto', 'descripcionProducto', 'estatus',)

admin.site.register(products, productosAdmin)