from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from finsee.utils.models import CreatedModified


class Expenditure(CreatedModified):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'expenditure'
        ordering = ['-id']


class ExpenditureIncome(CreatedModified):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'expenditure_income'
        ordering = ['-id']


class ExpenditureIncomeDetail(CreatedModified):
    name = models.CharField(max_length=128)
    amount = models.DecimalField(
        decimal_places=2, max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))])

    period = models.CharField(max_length=25, choices=[
        ('monthly', 'monthly'),
        ('once', 'Once'),
        ('daily', 'Daily')
    ])
    expenditure = models.ForeignKey(
        "ExpenditureIncome",
        on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = 'expenditure_income_detail'
        ordering = ['-id']


class ExpenditureOutcome(CreatedModified):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'expenditure_outcome'
        ordering = ['-id']


class ExpenditureOutcomeDetail(CreatedModified):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    rate = models.CharField(max_length=25, choices=[
        ('percentage', '%'),
        ('amount', 'Amount')
    ])
    outcome = models.ForeignKey(
        "expenditure.ExpenditureOutcomeDetail",
        on_delete=models.CASCADE, null=True)

    category = models.ForeignKey(
        "outcome.OutcomeCategory",
        null=True,
        blank=True,
        related_name="expenditure_category",
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    income = models.ForeignKey("expenditure.ExpenditureIncomeDetail", on_delete=models.CASCADE, null=True)

    account = models.CharField(max_length=6, choices=[
        ('credit', "credit"),
        ('debit', 'Debit')
    ])

    class Meta:
        db_table = 'expenditure_outcome_detail'
        ordering = ['-id']
