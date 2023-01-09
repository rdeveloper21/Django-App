from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'RutujP',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 10, 2022'
#     },
#     {
#         'author': 'RockyB',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 11, 2022'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})