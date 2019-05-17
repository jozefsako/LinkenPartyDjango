from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [

    # Default
    path('', views.index, name='index'),

    # Users
    path('allUsers', views.GetAllUsers),
    path('getUser', views.GetUser.as_view()),

    # Events
    path('allEvents', views.GetAllEvents),
    path('getEvent', views.GetEventByIdView),

    # Participations
    path('participations', views.GetAllParticipations),
]