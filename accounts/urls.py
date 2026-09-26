from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path 

from .forms import LoginForm
from . import views 


app_name = 'accounts'


urlpatterns = [
        path('register/', views.register, name='register'),
        path('login/', LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name='login'),
        path('logout/', view=LogoutView.as_view(), name='logout'),
        ]
