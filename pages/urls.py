from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ad/<int:pk>', views.Detail.as_view(), name='detail'),
    path('ad/', views.Post.as_view(), name='post'),
]
