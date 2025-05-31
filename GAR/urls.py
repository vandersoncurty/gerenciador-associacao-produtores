"""
URL configuration for GAR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework import routers
from apps.users.api import viewsets as user_viewsets
from apps.addresses.api import viewsets as address_viewsets
from apps.contacts.api import viewsets as contact_viewsets
from apps.roles.api import viewsets as role_viewsets
from apps.permissions.api import viewsets as permission_viewsets
from apps.member.api import viewsets as member_viewsets
from apps.slip_status.api import viewsets as slip_status_viewsets
from apps.slip.api import viewsets as slip_viewsets

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

route = routers.DefaultRouter()

route.register(r'users', user_viewsets.UserViewSet, basename='Users')
route.register(r'addresses', address_viewsets.AddressViewSet, basename='Addresses')
route.register(r'contacts', contact_viewsets.ContactViewSet, basename='Contacts')
route.register(r'roles', role_viewsets.RoleViewSet, basename='Roles')
route.register(r'permissions', permission_viewsets.PermissionViewSet, basename='Permissions')
route.register(r'members', member_viewsets.MemberViewSet, basename='Members')
route.register(r'slip-status', slip_status_viewsets.SlipStatusViewSet, basename='SlipStatus')
route.register(r'slips', slip_viewsets.SlipViewSet, basename='Slips')

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # API schema and documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API endpoints
    path('api/', include(route.urls)),
]
