"""
URL configuration for ecommerce_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home  # Import the home view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Include the accounts app URLs
    path('', home, name='home'),  # Root URL
    path('api/orders/', include('orders.urls')),  # Include orders app URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # To log in and get access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # To refresh access token
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# available api for accounts
# Now, the following endpoints will be available:

#     POST /api/accounts/auth/login/ for login
#     POST /api/accounts/auth/logout/ for logout
#     POST /api/accounts/auth/registration/ for registration


# avaliable api for orders