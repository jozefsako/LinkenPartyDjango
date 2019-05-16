from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.core import serializers
from django.conf import settings
from django.db import connection

def index(request):
    #GetAllUsers(request)
    my_custom_sql()
    return HttpResponse("Hello, world. You're at the polls index.")

def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchall()
    print(row)
    return row

def GetAllUsers(request):
    users = serializers.serialize('json', User.objects.all())
    cat = str(users)
    c = cat.replace('\'', '\"')
    return Response(json.loads(c), status=status.HTTP_200_OK)
