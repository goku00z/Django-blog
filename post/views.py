from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def all_post(request):
	posts = Article.objects.all()
	return render(request, 'post/index.html', {'posts': posts})



def post_detail(request, id):
	post = get_object_or_404(Article, id=id)

	return render(request, 'post/post_detail.html', {"post": post})