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

    return JsonResponse(serializer.data ,safe=False)

@api_view(['GET'])
def conversation_detail(request, id):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=id)
    
    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def conversation_send_message(request, id):
        conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=id)
        
        for user in conversation.users.all():
            if user != request.user:
                sent_to = user
        
        conversation_message = ConversationMessage.objects.create(
            conversation = conversation,
            body = request.data.get('body'),
            sent_to= sent_to,
            created_by = request.user
            
        )
    
        serializer = ConversationMessageSerializer(conversation_message)
        return JsonResponse(serializer.data, safe=False)