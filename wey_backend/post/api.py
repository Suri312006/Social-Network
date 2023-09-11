
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import PostForm
from .models import Post, Like
from .serializers import PostSerializer
from account.serializers import UserSerializer
from account.models import User

@api_view(['GET'])
def post_list(request):
    #shows only your posts and friends posts in feed
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    posts = Post.objects.filter(created_by_id__in=list(user_ids))
    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)

    
@api_view(['GET'])
def post_list_profile(request, id):
    
    user = User.objects.get(pk=id)
    
    posts = Post.objects.filter(created_by=id)
    
    posts_serializer = PostSerializer(posts, many=True)
    
    user_serializer = UserSerializer(user)
    
    
    
    return JsonResponse({
        'posts': posts_serializer.data, 
        'user': user_serializer.data
        }, safe=False)

@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        
        serializer = PostSerializer(post)
        
        return JsonResponse(serializer.data, safe=False)
    else:
    
        return JsonResponse({'error': 'fuck you'})
    

@api_view(['POST'])
def post_like(request, id):     
    # like = Like.objects.create(created_by=request.user)
    post = Post.objects.get(pk=id)
    like = Like.objects.create(created_by=request.user)

    
    if len(post.likes.filter(created_by=request.user)) == 0:
        post.likes.add(like)
        post.likes_count +=1
        post.save()
        return JsonResponse({'like_status': 'created'})
    else:
        return JsonResponse({'like_status': 'exists'})
    
   
    


    