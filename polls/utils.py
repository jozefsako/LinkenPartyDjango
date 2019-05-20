from polls.serializers import UserSerializer

def jwtHandler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }