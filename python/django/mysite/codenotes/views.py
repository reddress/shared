from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tag, Language, Post, Sample

# Create your views here.

def index(request):
    return render(request, 'codenotes/index.html')

@login_required
def view_post(request, post_id):
    post = Post.objects.get(user=request.user, pk=post_id)
    return render(request, 'codenotes/view_post.html',
                  { 'post': post })
    
