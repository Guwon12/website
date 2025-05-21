# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    movies = Movie.objects.all()  # Get all movies
    return render(request, 'movies/home.html', {'movies': movies})

# Movie detail
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Register page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})

# Add movie page
@login_required
def add_movie(request):
    # You can add logic to handle movie form and adding new movies
    pass

# Login redirect
def login_redirect(request):
    return redirect('home')

# User profile page
@login_required
def user_profile(request):
    return render(request, 'movies/profile.html')
