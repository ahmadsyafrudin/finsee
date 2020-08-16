from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from income.views import IncomeViewSet

router = routers.SimpleRouter(trailing_slash=True)

router.register("income", IncomeViewSet)


urlpatterns = [
    url("", include(router.urls)),
]
