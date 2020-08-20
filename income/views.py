from rest_framework import viewsets

from income.models import Income
from income.serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
