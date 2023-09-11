from .models import Post, Like, Comment
from rest_framework.serializers import ModelSerializer
from account.serializers import UserSerializer

class PostSerializer(ModelSerializer):
    
    created_by = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at_formatted', 'likes_count','comments_count')
        

class CommentsSerializer(ModelSerializer):
    created_by = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_by', 'created_at_formatted')

class PostDetailSerializer(ModelSerializer):
    comments = CommentsSerializer(read_only = True, many=True)
    created_by = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at_formatted', 'likes_count','comments')
        

