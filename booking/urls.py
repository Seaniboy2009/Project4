from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu/', views.MenuPage.as_view(), name='menu'),
    path('booking/', views.BookingPage.as_view(), name='booking'),
    path('management/', views.ManagementPage.as_view(), name='management'),
    path('mybookings/', views.MyBookingsPage.as_view(), name='mybookings')
]
