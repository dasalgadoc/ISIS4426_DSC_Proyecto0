""" App's Events URL """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Management user

    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='pforgot/',
        view=views.forgot_password,
        name='pforgot'
    )

]