from django.urls import path
from .views import MyAccountPageView, ReviewView


app_name = 'users'
urlpatterns = [
    path('my-account/', MyAccountPageView.as_view(), name='my_account'),
    path('reviews/', ReviewView.as_view(), name='reviews'),
]
