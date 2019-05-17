from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#class LoginSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ('username','password_user')
    
#    def validate_user:
#        user = None
#        user = authenticate(username = username, password = password)
#        if user is None:
#            raise ValueError('User unkown.')
#        return user