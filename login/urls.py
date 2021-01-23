from django.urls import path, include
from . import views

app_name = 'login'
urlpatterns = [  
    path('signup/', views.signup_view, name = 'signup'),
    path('signin/', views.signin_view, name = 'signin'),
    path('logout/', views.logout_view, name = 'logout'),
 
]