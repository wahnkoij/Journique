from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('pins/', pin_list, name='pin_list'),
    path('pin/<int:pin_id>/', pin_detail, name='pin_detail'),
    path('pin/add/', add_pin, name='add_pin'),
    path('profile/', profile_view, name='profile'),
    path('login/', login, name='login'),
    path('view_1/', view_1, name='view_1'),
    path('view_2/', view_2, name='view_2'),
    path('view_3/', view_3, name='view_3'),
    path('view_4/', view_4, name='view_4'),
    path('view_5/', view_5, name='view_5'),
]
