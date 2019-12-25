from django.shortcuts import render
from django.http import HttpResponse

# @shortucter4
# This is the view of Home page
def index(request):
	return render(request, 'homepage/index.html')

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
