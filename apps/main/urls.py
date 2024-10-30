from django.urls import path
from app.main.views import main

urlpatterns = [
    path('', main, name='main'),
]