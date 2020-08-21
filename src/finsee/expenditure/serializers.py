from rest_framework.serializers import ModelSerializer

from finsee.expenditure.models import Expenditure, ExpenditureIncome, ExpenditureIncomeDetail, ExpenditureOutcome, \
    ExpenditureOutcomeDetail


class ExpenditureSerializer(ModelSerializer):
    class Meta:
        model = Expenditure
        fields = "__all__"


class ExpenditureIncomeSerializer(ModelSerializer):
    class Meta:
        model = ExpenditureIncome
        fields = "__all__"


class ExpenditureIncomeDetailSerializer(ModelSerializer):
    class Meta:
        model = ExpenditureIncomeDetail
        fields = "__all__"


class ExpenditureOutcomeSerializer(ModelSerializer):
    class Meta:
        model = ExpenditureOutcome
        fields = "__all__"


class ExpenditureOutcomeDetailSerializer(ModelSerializer):
    class Meta:
        model = ExpenditureOutcomeDetail
        fields = "__all__"
