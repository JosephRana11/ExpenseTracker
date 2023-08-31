from django.shortcuts import render , redirect
from .models import Expense , Income
from .forms import IncomeForm , ExpenseForm
from Wallet.models import Wallet 

def record_income_view(request):
  if request.method == 'POST':
    owner_wallet = Wallet.objects.get(owner=request.user)
    form = IncomeForm(request.POST)
    if form.is_valid():
      print('form valid')
      data = form.save(commit=False)
      data.wallet_origin = owner_wallet
      data.save()
    return redirect('home')
  else:
   context = {
    'form': IncomeForm
   }
   return render(request , 'record-income.html' , context)

def record_expense_view(request):
  if request.method == 'POST':
    owner_walet = Wallet.objects.get(owner=request.user)
    form = ExpenseForm(request.POST)
    if form.is_valid():
      print('form valid')
      data = form.save(commit=False)
      data.wallet_origin = owner_walet
      data.save()
      return redirect('home')
  else:
   context = {
    'form': ExpenseForm
   }
   return render(request , 'record-expense.html', context)

def delete_income_view(request , obj_id):
  obj = Income.objects.get(pk = obj_id)
  obj.delete()
  return redirect('home')

def delete_expense_view(request , obj_id):
  obj = Expense.objects.get(pk = obj_id)
  obj.delete()
  return redirect('home')