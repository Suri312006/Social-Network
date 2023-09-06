from .models import Post
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'body', 'created_by', 'created_at',)

