from django.urls import include, path
from rest_framework import routers

from income.views import IncomeViewSet

router = routers.SimpleRouter(trailing_slash=True)

router.register("income", IncomeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
