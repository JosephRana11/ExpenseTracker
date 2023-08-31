from django.forms import ModelForm
from .models import Income , Expense

class IncomeForm(ModelForm):
  class Meta:
    model = Income
    fields = ['income_title' , 'income_amount']

class ExpenseForm(ModelForm):

  class Meta:
    model = Expense
    fields = ['expense_title' , 'expense_amount']