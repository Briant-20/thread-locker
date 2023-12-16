from . import views
from django.urls import path

urlpatterns = [
    path('', views.WishlistView.as_view(), name='Wishlist'),
]
