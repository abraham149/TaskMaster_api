# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.DetailUser.as_view()),
    path('me/', views.user_profile),
]