from rest_framework.serializers import ModelSerializer

from .models import User, FriendshipRequest

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')
        
class FriendshipRequestSerializer(ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)