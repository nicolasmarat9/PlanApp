
from django.urls import path, include
from . import views



app_name = 'Calendar'
urlpatterns = [
    
    path('home/', views.home, name = "home"),
    path('calendarprev/', views.calendarprev, name = "calendprev"),    
    path('calendarnext/', views.calendarnext, name = "calendnext"),
    path('calendar/', views.calendar, name = "calend"),
    path('calendar/<slug>/', views.session_list, name = "connect"),
    path('calendar/<slug>/<slugb>/', views.exercise_list, name = 'vecro'),
   
]

