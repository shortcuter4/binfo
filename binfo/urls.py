"""binfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# @shortcuter4
# Main URLS of a website are below, and when the user navigated to any of
# URLS below, such as 'homepage', it will check if there is any pattern
# that matches 'homepage' and if we do have a match , and the user wants
# to see '/homepage/' page, then this 'include()' function determines
# where the URLS is kept which is in 'homepage.urls' file , so it will
# process it


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls')),


# @shortcuter4	
# This (below) does not have to be written since it is already processed
# above..  'homepage.urls' - URLS!!!
	#path('homepage/login/', include('homepage.urls'))

# @shortcuter4
# This include function above allows us to add our list of URL patterns to
# specify which route should go to our 'homepage' URLS
]
