from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ad/<int:pk>', views.Detail.as_view(), name='detail'),
    path('new/', views.Post.as_view(), name='post'),
    path('search/', views.SearchViews, name='search-item'),
    path('salomatlik/', views.Salomatlik.as_view(), name='salomatlik'),
    path('kitoblar/', views.Kitoblar.as_view(), name='kitoblar'),
    path('quron/', views.Quron.as_view(), name='quron'),
    path('uyvaoffis/', views.UyOffis.as_view(), name='uyoffis'),
    path('ibodat/', views.Ibodat.as_view(), name='ibodat'),
    path('sovga/', views.Sovga.as_view(), name='sovga'),
    path('parfyum/', views.Parfyum.as_view(), name='parfyum'),
    path('gozallik/', views.Gozallik.as_view(), name='gozallik'),
    path('salomatlik/<int:pk>', views.SalomatlikDetail.as_view(), name='salomatlikdetail'),
]
