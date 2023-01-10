from django.urls import path
from . import views

#app_name = "movie"
urlpatterns = [
    #path('review',views.home, name="review"),
    #path('success',views.success, name="success"),
    #path('rate/<int:id>',views.rate,name="rate"),
    #path('', views.index, name='index'),
    path('', views.index, name='review-index'),
]
