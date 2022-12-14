from django.urls import path
from . import views
from .views import MyAccountPageView, ReviewView, ReviewsPageView, ReviewListView
# from views import ReviewCreateView, ReviewUpdateView, record_review, vote
# from .views import (
#    JokeCreateView, JokeDetailView, JokeListView, JokeUpdateView
# )

app_name = 'users'
urlpatterns = [
    path('my-account/', MyAccountPageView.as_view(), name='my_account'),
    path('', ReviewListView.as_view(), name='list'),
    # Remember that only URL paths that begin with '/jokes/' will be handed
    # off to the URLConf of the jokes app, so '' will actually be '/jokes/'.
    path('reviews/', ReviewView.as_view(), name='reviews'),
    #path('reviews/', ReviewView.as_view(), name='reviews', views.record_score),
    path('reviewspage/', ReviewsPageView.as_view(), name='reviewspage'),
    #path('record-review/', record_review, name="record_review"),
    #path('record-vote/', vote, name='vote')
]
