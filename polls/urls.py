from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [

    # Default
    path('', views.index, name='index'),

    # Users
    path('allUsers', views.GetAllUsers),
    path('currentUser/', views.Current_user),
    path('getUser', views.GetUser.as_view()),
    path('users/', views.UserList.as_view()),
    path('register', views.insertUser),

    # Events
    path('allEvents', views.GetAllEvents),
    path('getEvent', views.GetEventByIdView),
    path('events/', views.EventList.as_view()),

    # Participations
    path('participations', views.GetAllParticipations),
]
