from django.urls import path
from .views import record_expense_view , record_income_view , delete_income_view , delete_expense_view

urlpatterns = [
  path('record-income/' , record_income_view , name = 'record-income'),
  path('record-expense/' , record_expense_view , name = 'record-expense'),
  path('delete-income/<int:obj_id>' ,  delete_income_view , name = 'delete-income'),
  path('delete-expense/<int:obj_id>' , delete_expense_view , name = 'delete-expense'),
]