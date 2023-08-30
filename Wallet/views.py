from django.shortcuts import render , redirect
from .forms import WalletForm

def create_wallet_view(request):
  if request.method == 'POST':
    form = WalletForm(request.POST)
    if form.is_valid():
      wallet_data = form.save(commit= False)
      wallet_data.owner = request.user
      wallet_data.save()
      return redirect('home')
  else: 
   context = {
    'form' : WalletForm
   }
   return render(request , 'create-wallet.html' , context)
