from django.urls import path
from users.views import MyAccountPageView

urlpatterns = [
    path('my_account/', MyAccountPageView.as_view(), name='my_account'),
]
