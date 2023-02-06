from django.urls import path
from . import views
# ?? I didn't need to import index(request) ??
from review.views import ReviewView, record_review



urlpatterns = [
    path('', views.index, name='review-index'),# http://127.0.0.1:8000/review/
    path('review/', ReviewView.as_view(), name='review'),
    path('record-review/', record_review, name="record-review"),
]
