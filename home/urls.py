from . import views
from django.urls import path

urlpatterns = [
    path('', views.indexView.as_view(), name='home'),
]
