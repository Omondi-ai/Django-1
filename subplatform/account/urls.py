from django.urls import path
from . import views

from django.contrib.auth import views as auth_views




urlpatterns =[
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),

# password management
# 1 - allow us to enter our email in order to receive a password reset link

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="account/password-reset.html"), name="reset_password"),

    # 2 - show a success message of sorts stating that email was sent to reset our password

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/password-reset-sent.html"), name="password_reset_done"),

# 3- send a link to our email so as to reset our passweord,we shall need to enter a new password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password-reset-form.html"), name="password_reset_confirm"),

    # 4- show a success message stting that our pssword was changed
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/password-reset-complete.html"), name="password_reset_complete"),

]
