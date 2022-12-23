"""djangovue_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from allauth.account import urls
#from django.urls import path
#from django.conf.urls import url, include

#from users.views import MyAccountPageView

urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    # User Management
    path('users/', include('users.urls')),
    # path('accounts/', include('users.urls')),
    # Don't have 2 'accounts/' urls. Fix it!
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('allauth.account.urls')),
    #path('my-account/', MyAccountPageView.as_view(), name='my_account'),
    #path('accounts/', include('allauth.urls')),
    # urlpatterns = [path("", include("allauth.account.urls"))]
    #url(r'^accounts/', include('allauth.urls')),
    # Local Apps
    path('', include("games.urls")),
    #path('', include("users.urls"))
]
"""
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
"""
