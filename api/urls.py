# api/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('', views.ListTask.as_view()),
    path('<int:pk>/', views.DetailTask.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]