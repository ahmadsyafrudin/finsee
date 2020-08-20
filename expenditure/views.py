from rest_framework import viewsets

from expenditure.models import Expenditure, ExpenditureIncome, ExpenditureIncomeDetail, ExpenditureOutcome, \
    ExpenditureOutcomeDetail
from expenditure.serializers import ExpenditureSerializer, ExpenditureOutcomeDetailSerializer, \
    ExpenditureOutcomeSerializer, ExpenditureIncomeDetailSerializer, ExpenditureIncomeSerializer


class ExpenditureViewSets(viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer


class ExpenditureIncomeViewSets(viewsets.ModelViewSet):
    queryset = ExpenditureIncome.objects.all()
    serializer_class = ExpenditureIncomeSerializer


class ExpenditureIncomeDetailViewSets(viewsets.ModelViewSet):
    queryset = ExpenditureIncomeDetail.objects.all()
    serializer_class = ExpenditureIncomeDetailSerializer


class ExpenditureOutcomeViewSets(viewsets.ModelViewSet):
    queryset = ExpenditureOutcome.objects.all()
    serializer_class = ExpenditureOutcomeSerializer


class ExpenditureOutcomeDetailViewSets(viewsets.ModelViewSet):
    queryset = ExpenditureOutcomeDetail.objects.all()
    serializer_class = ExpenditureOutcomeDetailSerializer
