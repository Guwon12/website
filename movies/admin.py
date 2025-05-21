from django.contrib import admin
from .models import Movie, Genre

admin.site.register(Movie)  # Đảm bảo Movie được đăng ký trong Django admin
admin.site.register(Genre)  # Đảm bảo Genre cũng được đăng ký
