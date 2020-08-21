from rest_framework import viewsets

from finsee.outcome.models import Outcome, OutcomeTemplate, OutcomeTemplateDetail, OutcomeCategory
from finsee.outcome.serializers import OutcomeSerializer, OutcomeTemplateSerializer, OutcomeTemplateDetailSerializer, \
    OutcomeCategorySerializer


class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer


class OutcomeTemplateViewSet(viewsets.ModelViewSet):
    queryset = OutcomeTemplate.objects.all()
    serializer_class = OutcomeTemplateSerializer


class OutcomeTemplateDetailViewSet(viewsets.ModelViewSet):
    queryset = OutcomeTemplateDetail.objects.all()
    serializer_class = OutcomeTemplateDetailSerializer


class OutcomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = OutcomeCategory.objects.all()
    serializer_class = OutcomeCategorySerializer
