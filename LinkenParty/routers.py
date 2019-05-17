from rest_framework import routers
from polls.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'User',UserViewSet)