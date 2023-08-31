from django.urls import path
from .views import record_expense_view , record_income_view

urlpatterns = [
  path('record-income/' , record_income_view , name = 'record-income'),
  path('record-expense/' , record_expense_view , name = 'record-expense')
]