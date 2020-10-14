from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('tweets/', views.tweetListView, name='tweets'),
    path('tweets/<str:id>/', views.tweetDetailView, name='tweet_detail_view'),
]
