from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import ConversationMessageSerializer, ConversationSerializer, ConversationDetailSerializer
from .models import Conversation, ConversationMessage
from account.models import User

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
    
@api_view(['GET'])
def conversation_get_or_create(request, user_id):
    user = User.objects.get(pk=user_id)
    
    conversations = Conversation.objects.filter(users__in=list([request.user])).filter(users__in=list([user]))
    
    if conversations.exists():
        conversation = conversations.first()
        
    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user, request.user)
        conversation.save()

    serializer = ConversationDetailSerializer(conversation)
        
    return JsonResponse(serializer.data, safe=False)