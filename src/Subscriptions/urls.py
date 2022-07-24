from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="subs_dashboard"),
    path('subscriptions/create/', views.create_subscription, name="subs_create"),
    path('subscriptions/delete/<int:id>/', views.delete_subscription, name="subs_delete"),
]
