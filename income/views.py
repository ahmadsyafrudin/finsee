from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from rest_framework import viewsets

from income.models import Income
from income.serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
