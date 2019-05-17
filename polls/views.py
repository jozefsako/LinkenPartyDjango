from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import UserSerializer, EventSerializer, ParticipationSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.core import serializers
from django.conf import settings
from django.db import connection
from .models import AUsers, Events, Participations


def index(request):
    #GetAllUsers(request)
    my_custom_sql()
    GetAllEvents()
    return HttpResponse("Hello, world. You're at the polls index.")


def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchall()
    print(row)
    return row


@api_view(['GET'])
def GetAllUsers(request):
    users = serializers.serialize('json', AUsers.objects.all())
    cat = str(users)
    c = cat.replace('\'', '\"')
    return Response(json.loads(c), status=status.HTTP_200_OK)


class GetUser(APIView):
    def post(self, request, format=None):
        print(request)
        id_user = request.data['id_user']
        user = AUsers.objects.filter(id=id_user)
        prodSer = serializers.serialize('json', user)
        pro = str(prodSer)
        p = pro.replace('\'', '\"')
        return Response(json.loads(p), status=status.HTTP_200_OK)


@api_view(['GET'])
def GetAllEvents(request):
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM events")
    #     row = cursor.fetchall()
    # print(row)
    # return row
    events = serializers.serialize('json', Events.objects.all())
    cat = str(events)
    c = cat.replace('\'', '\"')
    return Response(json.loads(c), status=status.HTTP_200_OK)


@api_view(['GET'])
def GetEventByIdView(request):
    return 0


@api_view(['GET'])
def GetAllParticipations(request):
    return 0


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
