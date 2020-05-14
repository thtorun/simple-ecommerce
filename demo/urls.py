from django.urls import path

from eshop.demo import views
from django.urls import path

from eshop.demo import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add', views.add, name='add')
]