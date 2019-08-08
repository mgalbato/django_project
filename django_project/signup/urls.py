from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='signup-home'),
    path('confirm/', views.confirm, name='signup-confirm'),
]
