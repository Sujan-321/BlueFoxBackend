from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),  # For login, logout, etc.
    path('auth/registration/', CustomRegisterView.as_view(), name='custom_registration'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
]


# Testing the API

#     GET /api/accounts/profile/: To view the current user's profile.
#     PUT /api/accounts/profile/: To update the current user's profile information (like phone_no, address, and profile_img).