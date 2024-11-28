from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('Productos/', views.Productos, name='Productos'),  # This will match the URL '/principal/'
    path('Productos/ProductoDetalle/<int:codigoProducto>', views.ProductoDetalle, name='ProductoDetalle'),
]
 