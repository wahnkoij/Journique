from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('users/', user_list, name='user_list'),
    path('users/<str:username>/', user_profile, name='user_profile'),
    path('search_users/', search_users, name='search_users'),
    # pins
    path('pin/add/', add_pin, name='add_pin'),
    path('pins/', pin_list, name='pin_list'),
    path('pin/<int:pin_id>/', pin_detail, name='pin_detail'),
    path('pin/<int:pin_id>/edit/', edit_pin, name='edit_pin'),
    path('pin/<int:pin_id>/delete/', delete_pin, name='delete_pin'),
    # profile interaction
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('page_not_found_404/', page_not_found_404, name='404_error'),
]
