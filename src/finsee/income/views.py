from rest_framework import viewsets

from finsee.income.models import Income
from finsee.income.serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
