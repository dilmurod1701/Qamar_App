from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('advertise/<int:pk>', views.Detail.as_view(), name='detail'),
    path('advertise/', views.Post.as_view(), name='post'),
    path('advertise/quronikarim', views.Quron.as_view(), name='quron'),
]
