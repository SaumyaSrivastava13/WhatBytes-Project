from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordResetDoneView, 
    PasswordResetConfirmView, PasswordResetCompleteView
)
from .forms import CustomUserCreationForm

class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class ForgotPasswordView(PasswordResetView):
    template_name = 'accounts/forgot_password.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class ChangePasswordView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'accounts/change_password.html', {'form': form})

class DashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'accounts/dashboard.html')

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'accounts/profile.html', {'user': request.user})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/forgot_password.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
