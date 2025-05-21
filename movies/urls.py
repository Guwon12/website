from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),  # Đường dẫn cho trang thêm phim
    path('login_redirect/', views.login_redirect, name='login_redirect'),
    path('profile/', views.user_profile, name='profile'),
]
