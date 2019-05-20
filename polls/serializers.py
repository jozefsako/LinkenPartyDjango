from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AUsers, Events, Participations, AUsersWithouID
from rest_framework_jwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many = True,
        model = AUsers
        fields = '__all__'

class UserSerializerWithoutID(serializers.ModelSerializer):
    class Meta:
        model = AUsersWithouID
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "username",
            "type_user",
            "registration_date",
            "birthdate",
            "phone",
            "gender",
            "version_number")


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


class AUserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password_user = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password_user is not None:
            instance.set_password_user(password_user)
        instance.save()
        return instance

    class Meta:
        model = AUsers
        fields = ("token",
            "id_user" 
            "first_name",
            "last_name",
            "email",
            "password_user",
            "username",
            "type_user",
            "registration_date",
            "birthdate",
            "phone",
            "gender",
            "version_number")


    #    model = AUsers
    #     fields = ("token"
    #               "first_name",
    #               "last_name",
    #               "email",
    #               "password_user",
    #               "username",
    #               "type_user",
    #               "registration_date",
    #               "birthdate",
    #               "phone",
    #               "gender",
    #               "version_number")
