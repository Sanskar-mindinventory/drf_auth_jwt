from django.urls import path
from Authentication.views import CreateUserView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('create', CreateUserView.as_view(), name='create-user'),
    path('user/<int:id>', UserView.as_view(), name='get-user'),

    # JWT Token Paths
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
