from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.create_post, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),

]
