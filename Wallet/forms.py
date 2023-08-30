from django.forms import ModelForm
from .models import Wallet

class WalletForm(ModelForm):
  class Meta:
    model = Wallet
    fields = ['wallet_name' , 'amount']