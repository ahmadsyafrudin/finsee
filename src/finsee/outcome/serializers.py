from rest_framework.serializers import ModelSerializer

from finsee.outcome.models import Outcome, OutcomeTemplate, OutcomeTemplateDetail, OutcomeCategory


class OutcomeSerializer(ModelSerializer):
    class Meta:
        model = Outcome
        fields = "__all__"


class OutcomeTemplateSerializer(ModelSerializer):
    class Meta:
        model = OutcomeTemplate
        fields = "__all__"


class OutcomeTemplateDetailSerializer(ModelSerializer):
    class Meta:
        model = OutcomeTemplateDetail
        fields = "__all__"


class OutcomeCategorySerializer(ModelSerializer):
    class Meta:
        model = OutcomeCategory
        fields = "__all__"
