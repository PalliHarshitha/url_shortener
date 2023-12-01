from django.urls import path
from .views import home, createShortURL, redirect

urlpatterns = [
    path('', createShortURL, name='create'),  # Redirect root URL to createShortURL
    path('create/', createShortURL, name='create'),
    path('<str:url>', redirect, name='redirect')
]