from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.serializers import UserSerializer, GroupSerializer

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.active()
    return render(request, 'blog/post_list.html', {'posts': posts})

def toggle_like(request, post_id, does_like):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
      post.likes.add(request.user)
    else:
      post.likes.remove(request.user)
    #TODO return a response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
