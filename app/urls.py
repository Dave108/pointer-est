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
                  path('my-pins/', views.my_pins, name="my-pins"),
                  path('create-pin/', views.create_pin, name="create-pin"),
                  path('fav-pin/<int:pk>/', views.fav_pin, name="fav-pin"),
                  path('my-fav-pins/', views.my_fav_pins, name="my-fav-pins"),
                  path('create-board/', views.create_board, name="create-board"),
                  path('search-pins/', views.search_pins, name="search-pins"),
                  path('pin-page/<slug>/', views.pin_page, name="pin-page"),
                  path('my-pins/<slug>/', views.open_folder, name="board-open"),  # for opening folders and checking their images
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
