from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking_view, name='booking')

]