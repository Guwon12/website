from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Movie
from .forms import MovieForm

def home(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query).order_by('title')  # Thêm order_by để sắp xếp theo title
    else:
        movies = Movie.objects.all().order_by('created_at')  # Sắp xếp theo ngày tạo

    paginator = Paginator(movies, 5)  # Hiển thị 5 phim mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movies/home.html', {'page_obj': page_obj})

def user_profile(request):
    # Render trang hồ sơ người dùng
    return render(request, 'accounts/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tài khoản của bạn đã được tạo thành công! Bạn có thể đăng nhập ngay.')
            return redirect('login')  # Sau khi đăng ký thành công, chuyển hướng đến trang đăng nhập
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def login_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(reverse('admin:index'))  # Chuyển đến trang admin nếu là admin
        else:
            return redirect('home')  # Chuyển đến trang chủ nếu là người dùng bình thường
    else:
        return redirect('login')  # Nếu chưa đăng nhập, chuyển đến trang đăng nhập



def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)  # Đảm bảo rằng bạn xử lý request.FILES
        if form.is_valid():
            form.save()  # Lưu phim vào cơ sở dữ liệu
            return redirect('home')  # Chuyển hướng đến trang home
    else:
        form = MovieForm()  # Hiển thị form cho lần truy cập đầu tiên

    return render(request, 'movies/add_movie.html', {'form': form})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


