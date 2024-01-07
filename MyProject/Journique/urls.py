from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', home, name='home'),
    path('users/', user_list, name='user_list'),
    path('users/<str:username>/', user_profile, name='user_profile'),
    path('search/', search_results, name='search_results'),
    # pins
    path('pin/add/', add_pin, name='add_pin'),
    path('my_pins/', MyPinsView.as_view(), name='my_pins'),
    path('pins/', pin_list, name='pin_list'),
    path('pin/<int:pin_id>/', pin_detail, name='pin_detail'),
    path('pin/<int:pin_id>/edit/', edit_pin, name='edit_pin'),
    path('pin/<int:pin_id>/delete/', delete_pin, name='delete_pin'),
    path('category/<int:category_id>/pins/', category_pins, name='category_pins'),
    # profile interaction
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('password/change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('select_preferred_categories/', select_preferred_categories, name='select_preferred_categories'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('page_not_found_404/', page_not_found_404, name='404_error'),
    # superuser
    path('superuser/pins/', superuser_pin_management, name='superuser_pin_management'),
    path('superuser/categories/', superuser_category_management, name='superuser_category_management'),
    path('superuser/categories/edit/<int:category_id>/', edit_category, name='edit_category'),
    path('superuser/categories/delete/<int:category_id>/', delete_category, name='delete_category'),
]
