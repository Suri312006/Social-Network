from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm

from .models import FriendshipRequest, User


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    

    if form.is_valid():
        form.save()

        # Send verification email later!
    else:
        message = 'error'
    
    return JsonResponse({'message': message})

@api_view(['POST'])
def send_friend_request(request, pk):
    
    user = User.objects.get(pk=pk)
    
    friendship_request = FriendshipRequest(created_for=user, created_by=request.user)
    

    
    return JsonResponse({'Friendship Request Created Between' : f"{user.id} and {request.user.id}"})