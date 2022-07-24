from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("Users.urls")),
    path('dashboard/', include("Subscriptions.urls")),
    path('', views.index, name="index"),
]
