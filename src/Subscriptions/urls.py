from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="subs_dashboard"),
    path('create/', views.create_subscription, name="subs_create"),
    path('delete/<int:id>/', views.delete_subscription, name="subs_delete"),
]
