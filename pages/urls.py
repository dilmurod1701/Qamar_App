from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/<int:pk>', views.Detail.as_view(), name='detail'),
    path('new/', views.Post.as_view(), name='post'),
    path('category/<str:cats>', views.CategoryView, name='category'),
    path('search/', views.SearchViews, name='search-item'),
    path('products/search/', views.SearchViews, name='search-item'),
]
