from django.urls import path

from .views import AboutView, ContactView, HomePageView

app_name = 'pages'
urlpatterns = [
    # Check djangovue/urls.py
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('games/', AboutView.as_view(), name='games'),
]
