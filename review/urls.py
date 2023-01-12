from django.urls import path
from . import views
# ?? I didn't need to import index(request) ??
from review.views import ReviewView, record_review
#from . import ReviewView, record_review

#app_name = "movie"
urlpatterns = [
    #path('review',views.home, name="review"),
    #path('success',views.success, name="success"),
    #path('rate/<int:id>',views.rate,name="rate"),
    #path('', views.index, name='index'),
    path('', views.index, name='review-index'),# http://127.0.0.1:8000/review/
    #path('', ReviewView.as_view(), name='review-index'),# http://127.0.0.1:8000/review/
    path('review/', ReviewView.as_view(), name='review'),
    #path('record-review/', record_review, name="record-review"),
    path('record-review/', record_review, name="record-review"),
]
