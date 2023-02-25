from django.urls import path,include
from homeApp import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('<slug:c_slug>',views.home,name='prod_cat'),
    path('<slug:c_slug>/',views.products,name='prod_cat'),
    path('<slug:c_slug>/<slug:prod_slug>/',views.prodDetails,name='details'),
    path('search',views.search,name='search')
]