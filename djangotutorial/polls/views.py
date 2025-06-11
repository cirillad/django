from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, PostForm
from django.contrib import messages
from .models import CustomUser, Post
from .utils import optimize_image
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('polls:index')  # або куди хочеш після логіну
        else:
            messages.error(request, 'Невірний логін або пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']

                if 'image' in request.FILES:
                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(300, 300))
                    user.image_small.save(new_name, optimized_image, save=False)

                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(600, 600))
                    user.image_medium.save(new_name, optimized_image, save=False)

                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(1200, 1200))
                    user.image_large.save(new_name, optimized_image, save=False)

                user.save()
                return redirect('polls:index')
            except Exception as e:
                messages.error(request, f'Помилка при реєстрації: {str(e)}')
        else:
            messages.success(request, 'Виправте помилки в формі')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('polls:index')

def users(request):
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('polls:post_list')
    else:
        form = PostForm()
    # Звертаємось без префікса 'polls/' бо шаблони у кореневій папці templates/
    return render(request, 'create_post.html', {'form': form})

def post_list(request):
    posts = Post.objects.select_related('author').order_by('-created_at')
    # Аналогічно тут — без 'polls/'
    return render(request, 'post_list.html', {'posts': posts})
