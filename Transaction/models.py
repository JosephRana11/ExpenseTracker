from django.db import models
from Wallet.models import Wallet


class Income(models.Model):
  wallet_origin = models.ForeignKey(Wallet,  on_delete=models.CASCADE)
  income_tittle = models.CharField(max_length=200)
  income_amount = models.DecimalField(max_digits=10 , decimal_places=2)
  income_date = models.DateField(auto_now_add=True)

class Expense(models.Model):
  wallet_origin = models.ForeignKey(Wallet,  on_delete=models.CASCADE)
  expense_tittle = models.CharField(max_length=200)
  expense_amount = models.DecimalField(max_digits=10 , decimal_places=2)
  expense_date = models.DateField(auto_now_add=True)
