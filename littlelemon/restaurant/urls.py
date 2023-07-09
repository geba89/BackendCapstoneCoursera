from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import say_hello, index, SingleMenuItemView, MenuItemView, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello', say_hello, name='say_hello'),
    path('', index, name="index"),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),    
    path('api-token-auth/', obtain_auth_token),
]

router = DefaultRouter()
router.register(r'tables', BookingViewSet)
