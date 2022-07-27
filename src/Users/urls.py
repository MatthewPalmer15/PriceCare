from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_user, name='users_profile'),
    path('register/', views.register_user, name="users_register"),
    path('login/', views.login_user, name="users_login"),
    path('logout/', views.logout_user, name="users_logout"),
    path('delete/', views.delete_user, name='users_delete'),
    path('change/details', views.change_user_details, name='users_change_details'),
    path('change/password', views.change_user_password, name='users_change_password'),

    path('support/', views.view_support, name="users_support"),
    path('support/create/', views.create_support_ticket, name="usrers_create_support"),
    path('support/close/<int:ticket_id>', views.close_support_ticket, name="users_close_support"),
]
