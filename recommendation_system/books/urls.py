from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),  # Define the 'login' URL pattern
    path('signup/', views.register_page, name='register_page'),
    path('admin/', admin.site.urls),
    # Other URL patterns...
]
