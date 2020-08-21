from django.urls import include, path
from rest_framework import routers

from finsee.expenditure.views import ExpenditureViewSets, ExpenditureIncomeViewSets, ExpenditureIncomeDetailViewSets, \
    ExpenditureOutcomeViewSets, ExpenditureOutcomeDetailViewSets

router = routers.SimpleRouter()

router.register("expend", ExpenditureViewSets)
router.register("expend-income", ExpenditureIncomeViewSets, basename='expend-income')
router.register("expend-income-detail", ExpenditureIncomeDetailViewSets, basename='expend-income-details')
router.register("expend-outcome", ExpenditureOutcomeViewSets, basename='expend-outcome')
router.register("expend-outcome-detail", ExpenditureOutcomeDetailViewSets, basename='expend-outcome-details')

urlpatterns = [
    path("", include(router.urls)),
]
