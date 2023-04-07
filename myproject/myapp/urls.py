from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import post_list, post_detail, post_create, post_edit, post_delete, search_posts

app_name = 'myapp'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post_create/', views.post_create, name='post_create'),
    path('search/', search_posts, name='search_posts'),
        path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
       path('profile/<str:username>/', views.profile, name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
