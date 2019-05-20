from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import UserSerializer, EventSerializer, ParticipationSerializer, AUserSerializerWithToken, UserSerializerWithoutID
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.core import serializers
from django.conf import settings
from django.db import connection
from .models import AUsers, Events, Participations, AUsersWithouID


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
    formated_output = output.replace('\'', '\"')
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)

# Get all the Events
# param: request
@api_view(['GET'])
def GetAllEvents(request):
    events = serializers.serialize('json', Events.objects.all())
    output = str(events)
    formated_output = output.replace('\'', '\"')
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


@api_view(['GET'])
def GetEventByIdView(request):
     id_event = request.data['id_event']
     events = serializers.serialize(
         'json', Events.objects.filter(id_event=id_event))
     output = str(events)
     formated_output = output.replace('\'', '\"')
     return Response(json.loads(formated_output), status=status.HTTP_200_OK)


# Get all the Participations of Events
# param: request
@api_view(['GET'])
def GetAllParticipations(request):
    participations = serializers.serialize(
        'json', Participations.objects.all())
    output = str(participations)
    formated_output = output.replace('\'', '\"')
    return Response(json.loads(formated_output), status=status.HTTP_200_OK)


class GetUser(APIView):
    def post(self, request, format=None):
        id_user = request.data['id_user']
        aUser = AUsers.objects.filter(id=id_user)
        aUser_serialized = serializers.serialize('json', aUser)
        aUser_str = str(aUser_serialized)
        formated_user = aUser_str.replace('\'', '\"')
        return Response(json.loads(formated_user), status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = AUsers.objects.all()
    serializer_class = UserSerializer


# UserList
class UserList(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        aUser = AUsers.objects.filter(username=username)
        aUser_serialized = serializers.serialize('json', aUser)
        aUser_str = str(aUser_serialized)
        formated_user = aUser_str.replace('\'', '\"')
        jsonUser = json.loads(formated_user)
        if(jsonUser[0]['fields']['password'] == password):
             return Response(json.loads(formated_user), status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = UserSerializerWithoutID(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# EventList
class EventList(APIView):
    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = EventSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        id_event = request.data['id_event']
        events = serializers.serialize(
            'json', Events.objects.filter(id_event=id_event))
        output = str(events)
        formated_output = output.replace('\'', '\"')
        return Response(json.loads(formated_output), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
