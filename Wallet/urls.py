from django.urls import path
from .views import create_wallet_view

urlpatterns = [
  path('create-wallet' , create_wallet_view , name = 'create-wallet')
]