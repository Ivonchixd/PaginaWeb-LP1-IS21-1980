from django.urls import path
from . import views
urlpatterns = [
    path('', views.Productos, name='Productos'),  # This will match the URL '/principal/'
    path('Principal/', views.index, name='index'),
]
 