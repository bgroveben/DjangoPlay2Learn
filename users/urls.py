from django.urls import path
# from . import views

from .views import CustomPasswordChangeView, MyAccountPageView, LoginPageView, SignupPageView

# https://www.youtube.com/watch?v=5guJFS0dsHY   2:24

# from . import views
# from allauth.account.views import LoginView, ConfirmEmailView

urlpatterns = [
    #path('email/verify', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path(
        "password/change/", CustomPasswordChangeView.as_view(),
        name="account_change_password"
    ),
    path('my-account/', MyAccountPageView.as_view(), name='my_account'),
    path('login/', LoginPageView.as_view(), name='login'),
    #path('login/', views.LoginView.as_view(template_name='my_custom_template.html'), name='login')
    path('signup/', SignupPageView.as_view(), name='signup')
]


"""
https://stackoverflow.com/questions/58029272/django-redirect-user-after-login/58029365#58029365
urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='account/login.html'),
        name='login',
    ),
    path(
        'logged-in/',
        <Your LoginView>,
        name='logged_in',
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
    ),
]
"""
