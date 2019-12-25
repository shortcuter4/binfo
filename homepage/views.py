from django.shortcuts import render
from django.http import HttpResponse

# @shortcuter4
# These are fake posts in the forum
posts = [
	{	
		'author': 'CS student',
		'title': 'Django development event',
		'content': 'Syllabus',
		'date_posted': '25 Dec, 2019'
	},
	{
		'author': 'CS student',
		'title': 'About Python course',
		'content': 'Lab content',
		'date_posted': '07 Dec, 2019'
	}
]

# @shortucter4
# This is the view of Home page
def index(request):
	context = {
		'posts': posts
	}
	return render(request, 'homepage/index.html', context)

# @shortcuter4
# NOTE: This is a temporary page, for a trial
# Login page is considered to do as a new app in different folder
# rather than inside 'homepage' folder
def login(request):
	return render(request, 'homepage/login.html')

# @shortcuter4
# This is the view of About page
def about(request):
	return render(request, 'homepage/about.html')
