from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('home/',views.homepage,name='home'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logouts,name='logout'),
    path('createclass/',views.createclass,name='createclass'),
]