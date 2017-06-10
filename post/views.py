from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-tarih')
    return render(request,'post/home.html',{'posts':posts})

def post_ayrintilar(request, post_id):
    post = get_object_or_404(Post , pk=post_id)
    return render(request , 'post/post_ayrinti.html', {'post':post})
