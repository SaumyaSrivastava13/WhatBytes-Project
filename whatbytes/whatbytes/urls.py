from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

def redirect_to_accounts(request, path=None):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    re_path(r'^.*$', redirect_to_accounts),
]
