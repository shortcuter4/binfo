from django.urls import path
from . import views

urlpatterns = [

	# @shortcuter4
	# Inside the path, the first string is empty because this file is already
	# processed the 'homepage' part and it is mandatory to keep it empty

	# @shortcuter4
	# The pattern (the empty string) is handled by a function 'views.index'
	# so we can navigate to 'views.py', and inside there is that 'index()'
	# function which determines what to return to 'homepage' page

	# @shortcuter4
	# it will navigate to      ->    .../homepage
	path('', views.index, name='home-index'),
	
	# @shortcuter4
	# it will navigate to      ->    .../homepage/login
	path('login/', views.login, name='home-login'),

	# @shortcuter4
	# it will naviage to       ->    .../homepage/about
	path('about/', views.about, name='home-about'),
]