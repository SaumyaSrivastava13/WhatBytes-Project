from django.urls import path
from .views import (
    CustomLoginView, SignUpView, ForgotPasswordView,
    CustomPasswordResetConfirmView, CustomPasswordResetDoneView,
    CustomPasswordResetCompleteView, ChangePasswordView,
    DashboardView, ProfileView, LogoutView
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot-password/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
