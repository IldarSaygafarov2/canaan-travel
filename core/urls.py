from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('reviews/', views.reviews_view, name="reviews"),
    path('booking/', views.booking_view, name="booking"),
    path('mission/', views.mission_view, name="mission"),
]