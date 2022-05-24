from django.urls import path
from . import views


# About URL Config
urlpatterns = [
	path('me/', views.me),
	path('another/', views.another),
]