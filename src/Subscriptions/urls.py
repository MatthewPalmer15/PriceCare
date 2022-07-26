from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="subs_dashboard"),
    path('create/', views.create_subscription, name="subs_create"),
    path('delete/<int:subscription_id>/', views.delete_subscription, name="subs_delete"),
    path('edit/<int:subscription_id>/', views.edit_subscription, name="subs_edit"),
    path('download/', views.download_statement, name="subs_download"),
]
