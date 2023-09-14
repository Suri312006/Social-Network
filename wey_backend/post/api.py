
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import PostForm
from .models import Post, Like, Comment, Trend
from .serializers import PostSerializer, PostDetailSerializer, CommentsSerializer, TrendSerializer
from account.serializers import UserSerializer
from account.models import User

@api_view(['GET'])
def post_list(request):
    #shows only your posts and friends posts in feed
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)
    
    posts = Post.objects.filter(created_by_id__in=list(user_ids))
        
    all_posts = Post.objects.all()
    
    trend = request.GET.get('trend', '')
    
    if trend:
        posts = all_posts.filter(body__icontains='#'+trend)

    
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
        
        user = request.user
        user.posts_count +=1

        user.save()
        
        print(user.posts_count)
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
    
   
@api_view(['GET'])
def post_detail(request, id):
    post = Post.objects.get(pk=id)
    
    return JsonResponse({
        'post': PostDetailSerializer(post).data    
        
    })
    
@api_view(['POST'])
def post_create_comment(request, id):
    #! PLEASE REMEMBER TO USE .OBJECTS.CREATE() WHEN MAKING A NEW THING FOR THE LOVE OF GOD
    comment = Comment.objects.create(created_by=request.user, body= request.data.get('body'))
    post = Post.objects.get(pk=id)
    
    
    post.comments_count +=1
    post.comments.add(comment)
    
    comment_serializer = CommentsSerializer(comment)

    
    post.save()
    print(request.data)
    return JsonResponse({'message': 'comment added',
                         'comment': comment_serializer.data
                         }, safe=False)
    
@api_view(['GET'])
def trends_list(request):
    
    trends = Trend.objects.all()
    
    serializer = TrendSerializer(trends, many=True)
    
    return JsonResponse(serializer.data, safe=False)