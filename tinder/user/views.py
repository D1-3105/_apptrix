from rest_framework import (generics,
                            permissions,

                            )
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class CreateUserView(generics.CreateAPIView):

    model= get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
