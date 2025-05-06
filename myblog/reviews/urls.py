from django.contrib import admin
from django.urls import include, path 
from .views import ReviewList

urlpatterns = [
    path('stream/<int:pk>/review/',ReviewList.as_view(),name= 'review_list'),
]