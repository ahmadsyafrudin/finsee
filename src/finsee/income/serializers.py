from rest_framework.serializers import ModelSerializer

from finsee.income.models import Income


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"
