from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blog.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.active()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    does_like = post.likes.filter(id=request.user.id).exists()
    if not does_like:
      post.likes.add(request.user)
      return redirect(post)
      #return render(request, 'blog/blog_detail.html', {'posts': post})
    else:
      post.likes.remove(request.user)
      return redirect(post)
      return HttpResponse('Didn\'t work')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})

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
