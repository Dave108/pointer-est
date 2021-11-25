from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home_view, name="homepage"),
                  path('user-logout/', views.logout_user, name="user-logout"),
                  path('user-login/', views.login_user, name="user-login"),
                  path('user-registration/', views.registration, name="user-registration"),
                  path('user-panel/', views.user_panel_view, name="user-panel"),
                  path('select-folder/', views.select_folder, name="select-folder"),
                  path('save-image/', views.save_image, name="save-image"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
