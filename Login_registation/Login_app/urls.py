from django.urls import path
from . import views

app_name = 'Login_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name ='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
