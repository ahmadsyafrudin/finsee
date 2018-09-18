from django.urls import path

from . import views


urlpatterns = [
    path("", views.ListIncome.as_view(), name="income-list"),
    path("add/", views.CreateIncome.as_view(), name="income-add"),
    path("update/<int:pk>/", views.UpdateIncome.as_view(), name="income-update")
]
