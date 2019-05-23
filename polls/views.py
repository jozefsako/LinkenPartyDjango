from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.core import serializers
from django.conf import settings
from django.db import connection
from .models import *
from datetime import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


# Get current AUser with JWT
# param: request
@csrf_exempt
@api_view(['GET'])
def Current_user(request):
    print(request.id_user)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# Get all the Users
# param: request
@api_view(['GET'])
def GetAllUsers(request):
    ausers = serializers.serialize('json', AUsers.objects.all())
    output = str(ausers)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Get all the Events
# param: request
@api_view(['GET', 'POST'])
def GetAllEvents(request):

    # Radian KM
    R = 6371

    if request.method == 'POST':
        currentDate = datetime.today().strftime('%Y-%m-%d')
        print(" DATE DU JOUR ", currentDate)
        st_event = 'Confirmed'

        lng = float(request.data['lng'])
        lat = float(request.data['lat'])
        d = float(request.data['distance'])
        r = float(d / R)
        lat_max = float(lat + r)
        lat_min = float(lat - r)
        lng_max = float(lng + r)
        lng_min = float(lng - r)

        query = "SELECT * from events where ( 6371 * acos( cos( radians(" + str(lat)+ ") ) * cos( radians( lat ) ) * cos( radians( lng ) - radians("+str(lng) +  ") ) + sin( radians( " + str(lat)+ ") ) * sin( radians( lat ) ) ) )  < "+ str(d)
        events = serializers.serialize('json', Events.objects.raw(query))
    
        output = str(events)
        #formated_output = output.replace('\'', '\"')
        #formated_output = output.replace("\\", r"\\")
        return Response(json.loads(output), status=status.HTTP_200_OK)

    elif request.method == 'GET':
        events = serializers.serialize('json', Events.objects.all())
        output = str(events)
        #formated_output = output.replace('\'', '\"')
        #formated_output = output.replace("\\", r"\\")
        return Response(json.loads(output), status=status.HTTP_200_OK)


# InsertEvent
@api_view(['POST'])
def insertEvent(request):
    serializer = EventSerializerWithoutID(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get the Event by an ID
# param: request that contains the id of the Event
@api_view(['GET'])
def GetEventById(request):
    id_event = request.data['id_event']
    events = serializers.serialize(
        'json', Events.objects.filter(id_event=id_event))
    output = str(events)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Get all Events created by a User
# param: request that contains the id of the user
@api_view(['GET', 'POST'])
def GetUserEvents(request):
    id_user = request.data['id_user']
    events = serializers.serialize('json', Events.objects.filter(id_user=id_user))
    output = str(events)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Get all the Events of a partygoer
# param: quest that contains the id of the user
@api_view(['GET', 'POST'])
def GetFetarEvents(request):
    id_user = request.data['id_user']
    events = serializers.serialize('json', Events.objects.raw(
        "SELECT * FROM events ev WHERE ev.id_event IN (SELECT par.id_event FROM participations par WHERE par.id_user = %s)", [id_user]))
    output = str(events)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def UpdateEvent(request):
    d = request.data
    Events.objects.filter(pk=request.data['id_event']).update(name_event=d['name_event'], theme_event=d['theme_event'], creation_date=d['creation_date'], start_date=d['start_date'], end_date=d['end_date'],price=d['price'], address_event=d['address_event'], size_hosting=d['size_hosting'], state_event=d['state_event'], description_event=d['description_event'], type_event=d['type_event'], lat=d['lat'], lng=d['lng'])
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def UpdateStateEvent(request):
    old_state = request.data['state_event']
    id_event = request.data['id_event']

    if(old_state == "Confirmed" or old_state == "confirmed"):
        Events.objects.filter(pk=request.data['id_event']).update(state_event='Canceled')
    else:
        Events.objects.filter(pk=request.data['id_event']).update(state_event='Confirmed')
        
    return Response(status=status.HTTP_200_OK)


# Get all the Participations of Events
# param: request
@api_view(['GET', 'POST'])
def GetAllParticipations(request):
    participations = serializers.serialize(
        'json', Participations.objects.all())
    output = str(participations)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Get all the Participations of the Event
# param: request
@api_view(['GET', 'POST'])
def GetEventParticipations(request):
    id_event = request.data['id_event']
    participations = serializers.serialize(
        'json', Participations.objects.filter(id_event=id_event))
    output = str(participations)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Get all the Participations of the User
# param: request
@api_view(['GET', 'POST'])
def GetUserParticipations(request):
    id_user = request.data['id_user']
    participations = serializers.serialize(
        'json', Participations.objects.filter(id_user=id_user))
    output = str(participations)
    #formated_output = output.replace('\'', '\"')
    formated_output = output.replace("\\", r"\\")
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Insert a new Participation for an user
# param: request that contains the id of the User and the Event
@api_view(['GET', 'POST'])
def insertParticipation(request):
    serializer = ParticipationSerializerWithoutID(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Add new user
# param: request
@api_view(['POST'])
def insertUser(request):
    serializer = UserSerializerWithoutID(data=request.data)

    #Checks if username or email already exists
    username = request.data['username']
    email = request.data['email']

    if(AUsers.objects.filter(username=username).count() > 0):
        return Response(status=status.HTTP_409_CONFLICT)

    elif(AUsers.objects.filter(email=email).count() > 0):
        return Response(status=status.HTTP_409_CONFLICT)

    elif serializer.is_valid():
        serializer.save()
        serializerTmp = UserSerializer(AUsers.objects.get(username=username))
        return Response(serializerTmp.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUser(APIView):
    def post(self, request, format=None):
        id_user = request.data['id_user']
        aUser = AUsers.objects.filter(id=id_user)
        aUser_serialized = serializers.serialize('json', aUser)
        aUser_str = str(aUser_serialized)
        #formated_user = aUser_str.replace('\'', '\"')
        formated_user = aUser_str.replace("\\", r"\\")
        return Response(json.loads(formated_user), status=status.HTTP_200_OK)


# UserList
class UserList(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        aUser = AUsers.objects.filter(username=username)
        aUser_serialized = serializers.serialize('json', aUser)
        aUser_str = str(aUser_serialized)
        #formated_user = aUser_str.replace('\'', '\"')
        formated_user = aUser_str.replace("\\", r"\\")
        jsonUser = json.loads(formated_user)
        if(jsonUser[0]['fields']['password'] == password):
             return Response(json.loads(formated_user), status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# EventList
class EventList(APIView):
    def get(self, request, format=None):
        id_event = request.data['id_event']
        events = serializers.serialize(
            'json', Events.objects.filter(id_event=id_event))
        output = str(events)
        #formated_output = output.replace('\'', '\"')
        formated_output = output.replace("\\", r"\\")
        return Response(json.loads(formated_output), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        id_event = request.data['id_event']
        events = serializers.serialize(
            'json', Events.objects.filter(id_event=id_event))
        output = str(events)
        #formated_output = output.replace('\'', '\"')
        formated_output = output.replace("\\", r"\\")
        return Response(json.loads(formated_output), status=status.HTTP_200_OK)
