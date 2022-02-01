from django.contrib import auth
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    path('logout/', views.logout_request, name= "logout"),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.post_index, name='post_index'),
    path('myposts/', views.my_posts, name="mypoems")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
