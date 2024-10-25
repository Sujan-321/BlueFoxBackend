from rest_framework import serializers
from .models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user", "first_name", "last_name", "email", "phone_no", "address", "profile_img"]

         
