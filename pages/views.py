from django.shortcuts import render , HttpResponse , redirect
from .forms import RegisterForm , LoginForm
from django.contrib.auth import login , logout , authenticate
from Wallet.models import Wallet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home_view(request):
  has_wallet = False
  if (request.user.is_authenticated):
   has_wallet = Wallet.objects.filter(owner=request.user).exists()
   print(has_wallet)
  context = {
    'has_wallet' : has_wallet
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