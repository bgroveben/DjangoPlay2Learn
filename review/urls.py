from django.urls import path
from . import views
# ?? I didn't need to import index(request) ??
from review.views import ReviewView, MyReviewsView, record_review


urlpatterns = [
    path('', views.index, name='review-index'),# http://127.0.0.1:8000/review/
    path('review/', ReviewView.as_view(), name='review'),
    path('myreviews/', MyReviewsView.as_view(), name='myreviews'),
    path('record-review/', record_review, name="record-review"),
    #path('reviews/', ReviewView.as_view(), name='reviews'),
    #path('reviewspage/', ReviewsPageView.as_view(), name='reviewspage'),
]
