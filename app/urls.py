from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # redirection facultative
    path('calculate-duration/', views.calculate_duration, name='calculate-duration'),
]
