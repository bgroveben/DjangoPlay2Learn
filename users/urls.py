from django.urls import path
from . import views
from .views import MyAccountPageView, ReviewsPageView, ReviewView


app_name = 'users'
urlpatterns = [
    path('my-account/', MyAccountPageView.as_view(), name='my_account'),

    path('reviews/', ReviewView.as_view(), name='reviews'),

    path('reviewspage/', ReviewsPageView.as_view(), name='reviewspage'),

]
