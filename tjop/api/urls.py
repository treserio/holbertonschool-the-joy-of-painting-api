from django.urls import path
from . import views

# app_name = 'api'

urlpatterns = [
    path('hex_values/', views.hex_values.as_view()),
]
