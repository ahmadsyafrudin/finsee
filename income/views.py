from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from income.forms import IncomeForm
from income.models import Income


class CreateIncome(CreateView):
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('income-list')


class ListIncome(ListView):
    model = Income
    paginate_by = 10


class UpdateIncome(UpdateView):
    model = Income
    fields = ["name", "amount", "income_type"]
    success_url = reverse_lazy('income-list')