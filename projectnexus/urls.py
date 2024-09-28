from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from restaurantsite.views import home, menu_view, signup, login_view, profile, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Login view can remain as the root
    path('signin/', login_view, name='signin'),  # Added signin path
    path('menu/', menu_view, name='menu'),
    path('profile/', profile, name='profile'),
    path('logout/', custom_logout, name='logout'),
    path('home/', home, name='index'),
    path('signup/', signup, name='signup'),
]