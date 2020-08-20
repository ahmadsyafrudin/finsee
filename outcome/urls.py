from django.urls import path, include
from rest_framework import routers

from outcome.views import OutcomeViewSet, OutcomeTemplateViewSet, OutcomeTemplateDetailViewSet, OutcomeCategoryViewSet

router = routers.SimpleRouter(trailing_slash=True)

router.register("outcome", OutcomeViewSet)
router.register("outcome-template", OutcomeTemplateViewSet)
router.register("outcome-template-details", OutcomeTemplateDetailViewSet)
router.register("outcome-category", OutcomeCategoryViewSet)


urlpatterns = [
    path("", include(router.urls))
]
