from django.urls import path
from registration import views

urlpatterns = [
    path('login', views.LogIn.as_view(), name='login'),
    path('logout', views.LogOut.as_view, name='logout'),
    path('sign', views.SignIn.as_view, name='sign')
]
