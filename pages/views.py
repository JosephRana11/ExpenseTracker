from django.shortcuts import render , HttpResponse , redirect
from .forms import RegisterForm , LoginForm
from django.contrib.auth import login , logout , authenticate
from Wallet.models import Wallet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Transaction.models import Income , Expense


def calculate_total(user_income , user_expense , balance):
  for item in user_income:
    balance += item.income_amount
  for item in user_expense:
    balance -= item.expense_amount
  return balance


def home_view(request):
  has_wallet = False
  if (request.user.is_authenticated):
   has_wallet = Wallet.objects.filter(owner=request.user).exists()
   if (has_wallet == True):
    user_wallet = Wallet.objects.get(owner=request.user)
    user_income = Income.objects.filter(wallet_origin=user_wallet)
    user_expense = Expense.objects.filter(wallet_origin=user_wallet)
    total_remaining_amt = calculate_total(user_income , user_expense , user_wallet.amount)
  context = {
    'has_wallet' : has_wallet , 
    'user_wallet' : user_wallet,
    'user_income' : user_income,
    'user_expense' : user_expense,
    'sum' : total_remaining_amt,
  }
  return render(request , 'home.html' , context)

def register_view(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      uname = form.cleaned_data['username']
      upass = form.cleaned_data['password1']
      user = authenticate(request , username = uname , password = upass)
      login(request , user)
      return redirect('home')
  else:
   context = {
    'form'  : RegisterForm
   }
   return render(request , 'register.html' , context)

def login_view(request):
  if request.method == 'POST':
    uname = request.POST.get('username')
    upass = request.POST.get('password')
    user = authenticate(request , username = uname , password = upass)
    if user is not None:
      login(request , user)
      return redirect('home')
    return redirect('login')
  else: 
    context = {
      'form': LoginForm
    }
    return render(request , 'login.html' , context)

def logout_view(request):
  logout(request)
  return redirect('register')

