from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm, ProfileForm

from .models import FriendshipRequest, User

from .serializers import UserSerializer, FriendshipRequestSerializer


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
    
    request_user = User.objects.get(pk=request.user.id)
    
    check1 = FriendshipRequest.objects.filter(created_for = request.user).filter(created_by=user)
    
    check2 = FriendshipRequest.objects.filter(created_for = user).filter(created_by=request.user)
    
    if check1.count() == 0 and check2.count() == 0 and request_user != user:

        friendship_request = FriendshipRequest.objects.create(created_for=user, created_by=request.user)
    
    else:
        return JsonResponse({'message': 'already exists'})
    

    
    return JsonResponse({'message': 'created'})


@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    friendship_requests = []
    
    if user == request.user:
        friendship_requests = FriendshipRequest.objects.filter(created_for=request.user, status=FriendshipRequest.SENT)
        
        
    friends = user.friends.all()
    
    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends':UserSerializer(friends, many=True).data,
        'requests': FriendshipRequestSerializer(friendship_requests, many=True).data,
    }, safe=False)
        
@api_view(['POST'])
def handle_request(request, pk, status):
    user = User.objects.get(pk=pk)
    sent_by_user = User.objects.get(pk=request.user.id)
    
    #saving status
    friendship_request = FriendshipRequest.objects.filter(created_for = request.user).get(created_by=user)
    friendship_request.status = status
    friendship_request.save()
    
    if(friendship_request.status == 'accepted'):
        #to add friends
        user.friends.add(request.user)
        
        
        
        #changing friend counts
        user.friends_count += 1
        sent_by_user.friends_count += 1
        
        user.save()
        sent_by_user.save()
        
        return JsonResponse({'message': 'request accepted'})


    if(friendship_request.status == 'rejected'):
        return JsonResponse({'message': 'request rejected'})
        
        
@api_view(['POST'])
def edit_profile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'email already exists'})
    else:
        print(request.FILES)
        print(request.POST)

        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

        return JsonResponse({'message': 'success'})
    
        

    
        
    
    
    