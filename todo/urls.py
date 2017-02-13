from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, kwargs={'authentication_form': LoginForm}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
]
