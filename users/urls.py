from django.urls import path

from .views import CustomPasswordChangeView, MyAccountPageView, LoginPageView, SignupPageView

urlpatterns = [
    path(
        "password/change/", CustomPasswordChangeView.as_view(),
        name="account_change_password"
    ),
    path('my-account/', MyAccountPageView.as_view(), name='my_account'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup')
]
