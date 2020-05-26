from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
import jwt
from .serializers import UserSerializer

# We could also use APIView, like the textbook, but CreateAPIView gives us a nicer form
class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
         # This will run our custom validation code
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    # This is not an endpoint, its a helper function used when we POST
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        # Check if there's a user with this email.
        user = self.get_user(email)
        # If this password is not the same as the password saved for the user
        # check_password is given to us by django.
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        # Create a JWT for the user, and send it back
        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})

# The register view simply creates a new user and sends back a success message if all is well, and any errors if not. 
# These errors might include the custom errors we just added to the UserSerializer.

# The login view finds the user by email and verifies their password with Django's check_password function that's automatically added to the user object. 
# If there's an error, we send back an error message, otherwise we create a token and send it back to the client in the response.
