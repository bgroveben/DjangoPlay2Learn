from django.urls import path
from . import views
from .views import MyAccountPageView, ReviewView, ReviewsPageView 
#record_review, vote


app_name = 'users'
urlpatterns = [
    path('my-account/', MyAccountPageView.as_view(), name='my_account'),
    path('reviews/', ReviewView.as_view(), name='reviews'),
    #path('reviews/', ReviewView.as_view(), name='reviews', views.record_score),
    path('reviewspage/', ReviewsPageView.as_view(), name='reviewspage'),
    #path('record-review/', record_review, name="record_review"),
    #path('record-vote/', vote, name='vote')
]
