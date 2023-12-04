from django.urls import path
from .views import pin_list, pin_detail, add_pin

urlpatterns = [
    path('pins/', pin_list, name='pin_list'),
    path('pin/<int:pin_id>/', pin_detail, name='pin_detail'),
    path('pin/add/', add_pin, name='add_pin'),
]
