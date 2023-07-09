from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import say_hello, index, SingleMenuItemView, MenuItemView, BookingViewSet

urlpatterns = [
    path('hello', say_hello, name='say_hello'),
    path('', index, name="index"),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),    
]

router = DefaultRouter()
router.register(r'tables', BookingViewSet)
