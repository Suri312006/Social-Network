from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import ConversationMessageSerializer, ConversationSerializer, ConversationDetailSerializer
from .models import Conversation, ConversationMessage


@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    print(conversations)

    serializer= ConversationSerializer(conversations, many=True)

    print(serializer.data)
    return JsonResponse(serializer.data ,safe=False)