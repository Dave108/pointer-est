from django.urls import path, include
from . import views
urlpatterns = [
    path('home-panel/', views.panel, name="home-panel"),
]
