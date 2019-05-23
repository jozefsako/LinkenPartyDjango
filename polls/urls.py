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
    path('allEvents', views.GetAllEvents), #Obtenir tous les events
    path('getEvent', views.GetEventById), #Obtenir un event {id_event}
    path('events/', views.EventList.as_view()), #
    path('addEvent', views.insertEvent), #Ajouter un event {json}
    path('eventParticipations', views.GetEventParticipations), 
    path('userParticipations', views.GetUserParticipations), #Participations d'un fetard 
    path('userEvents', views.GetUserEvents),   #Events créée par un user
    path('fetarEvents', views.GetFetarEvents), #Events d'un fetard 
    path('updateEvent', views.UpdateEvent),
    path('updateStateEvent', views.UpdateStateEvent),
    # path('eventsAndParticipations', views.GetEventsAndParticipations), #Events et le Nombre de Participations
    
    # Participations
    path('participations', views.GetAllParticipations), #Get all the participations in the system
    path('addParticipation', views.insertParticipation), #Add participation {json}
]
