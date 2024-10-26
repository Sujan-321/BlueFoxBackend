from rest_framework import generics, permissions, status
from .models import UserProfile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import HttpResponse
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
# import status

from dj_rest_auth.registration.views import RegisterView

class CustomRegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()  # or the appropriate model
    serializer_class = RegisterSerializer  # Make sure this serializer exists
    permission_classes = [AllowAny]  # Allows any user to access this endpoint
    
    def create(self, request, *args, **kwargs):
        # Validate and create the user using the serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(request)  # Create the user

        # Update the Django `User` model fields
        user.first_name = request.data.get('first_name', '')
        user.last_name = request.data.get('last_name', '')
        user.save()

        # Check if the UserProfile already exists for the user
        profile, created = UserProfile.objects.get_or_create(user=user)
        # Update the UserProfile fields
        profile.first_name = request.data.get('first_name', '')
        profile.last_name = request.data.get('last_name', '')
        profile.email = request.data.get('email', '')
        profile.phone_no = request.data.get('phone_no', '')
        profile.address = request.data.get('address', '')
        profile.save()

        # Return a response with user and profile details
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "email": profile.email,
                "phone_no": profile.phone_no,
                "address": profile.address,
            },
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)



def home(request):
    return HttpResponse("Welcome to the API!")

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile
