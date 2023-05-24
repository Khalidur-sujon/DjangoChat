from django.contrib.auth import views as auth_views
from django.urls import path
from .views import frontpage, signUp

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
