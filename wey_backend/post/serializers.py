from .models import Post, Like
from rest_framework.serializers import ModelSerializer
from account.serializers import UserSerializer

class PostSerializer(ModelSerializer):
    
    created_by = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at_formatted', 'likes_count',)
        

    

