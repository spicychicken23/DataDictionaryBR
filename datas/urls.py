from django.urls import path
from .views import dep_list, cif_list, fin_list, col_list, search_view
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('deposits/', dep_list, name='dep_list'),
    # path('depositproducts/', depro_list, name='depro_list'),
    path('cifs/', cif_list, name='cif_list'),
    path('financings/', fin_list, name='fin_list'),
    path('collaterals/', col_list, name='col_list'),
    path('search/', search_view, name='search'),
]