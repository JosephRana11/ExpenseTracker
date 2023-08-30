from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
  owner = models.OneToOneField(User , on_delete=models.CASCADE)
  wallet_name = models.CharField(max_length=200 , null=True , default= " Main Wallet")
  amount = models.DecimalField(max_digits=10 , decimal_places=2)
  date_create = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"Wallet owned by : {self.owner.username} Amount:{self.amount}"
  