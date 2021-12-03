from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home_view, name="homepage"),
                  path('user-page/', views.user_page, name="user-page"),
                  path('open-other-user/<user>/', views.open_other_user, name="open-other-user"),
                  path('edit-user/', views.edit_user, name="edit-user"),
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
                  path('like-comment/<slug>/<int:pk>/', views.like_comment, name="like-comment"),
                  path('pin-page/<slug>/', views.pin_page, name="pin-page"),
                  path('pin-comments/<int:pk>/', views.pin_comments, name="pin-comments"),
                  path('pin-comments/<int:pk>/<int:comment_pk>/', views.comments_reply, name="comments-reply"),
                  path('my-pins/<slug>/', views.open_folder, name="board-open"),  # for opening folders and checking their images
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
