from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import api

urlpatterns = [
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('signup/', api.signup, name='signup'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('me/', api.me, name='me'),
    
    path('friends/<uuid:pk>/', api.friends, name='friends'),
    path('friends/<uuid:pk>/request/', api.send_friend_request, name='send_friend_request'),
    
    
]