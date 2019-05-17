from rest_framework import serializers
from .models import AUsers, Events, Participations
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many = True,
        model = AUsers
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        many = True,
        model = Events
        fields = '__all__'


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        many = True,
        model = Participations
        fields = '__all__'
