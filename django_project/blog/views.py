from django.shortcuts import render
from .models import Post 
# posts = [
# 	{
# 		'title' : 'Blog Title 1',
# 		'author' : 'Name of Author 1',
# 		'date_posted' : 'March 18, 2022',
# 		'content' : 'Content of Post 1'
# 	},
# 	{
# 		'title' : 'Blog Title 2',
# 		'author' : 'Name of Author 2',
# 		'date_posted' : 'August 6, 2022',
# 		'content' : 'Content of Post 2'
# 	},
# 	{
# 		'title' : 'Blog Title 3',
# 		'author' : 'Name of Author 3',
# 		'date_posted' : 'October 2, 2022',
# 		'content' : 'Content of Post 3'
# 	}
# ]


def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About Page'})