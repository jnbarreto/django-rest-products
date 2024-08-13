from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
import logging

logger = logging.getLogger(__name__)


class RegistrationAPIView(APIView):
    """
    API Registration User - Create a new user
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SignInView(ObtainAuthToken):
    """
    API Sing in - login
    """

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(
                {'error': 'Username e password obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(
            {'error': f'Invalid credentials {username}, {password}'},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class SignOutView(APIView):
    """
    API Sing Out - login
    """

    def post(self, request):
        try:
            token_key = request.data.get('token')
            if not token_key:
                return Response(
                    {'error': 'Token obrigatório.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = Token.objects.get(key=token_key)
            token.delete()
            return Response(
                {'message': 'Successfully logged out'},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Token.DoesNotExist:
            return Response(
                {'error': 'Token Inválido.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
