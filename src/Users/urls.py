from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_user, name='users_profile'),
    path('register/', views.register_user, name="users_register"),
    path('login/', views.login_user, name="users_login"),
    path('logout/', views.logout_user, name="users_logout")
]
