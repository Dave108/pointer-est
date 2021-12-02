from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.panel, name="admin-panel"),
    path('page404/', views.show404, name="404-panel"),
]
