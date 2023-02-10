from django.urls import path
from . import views
# ?? I didn't need to import index(request) ??
from review.views import ReviewView, MyReviewsView, ReviewDeleteView


urlpatterns = [
    path('', views.index, name='review-index'),# http://127.0.0.1:8000/review/
    path('review/', ReviewView.as_view(), name='review'),
    path('myreviews/', MyReviewsView.as_view(), name='myreviews'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete'),
]
