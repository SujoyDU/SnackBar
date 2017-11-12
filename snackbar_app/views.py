
# Create your views here.
from rest_framework import viewsets
from . import serializers
from .models import UserProfile
from . import permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""
    serializer_class = serializers.UserProfileSerializer

    queryset = UserProfile.objects.all()
    # authentication_classes = (authentication.JSONWebTokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
