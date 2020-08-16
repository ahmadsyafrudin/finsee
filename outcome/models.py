from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from utils.models import CreatedModified


class OutcomeCategory(CreatedModified):
    name = models.CharField(max_length=128)
    period = models.CharField(max_length=25, choices=[
        ('monthly', 'monthly'),
        ('once', 'Once'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly')
    ])

    parent = models.ForeignKey(
        "outcome.OutcomeCategory",
        null=True,
        blank=True,
        related_name="detail",
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ['-id']
        db_table = 'outcome_category'


class Outcome(CreatedModified):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    rate = models.CharField(max_length=25, choices=[
        ('percentage', '%'),
        ('amount', 'Amount')
    ])
    category = models.ForeignKey(
        "outcome.OutcomeCategory",
        null=True,
        blank=True,
        related_name="category",
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))], null=True)

    account = models.CharField(max_length=6, choices=[
        ('credit', "credit"),
        ('debit', 'Debit')
    ])

    class Meta:
        ordering = ['-id']
        db_table = 'outcome'


class OutcomeTemplate(CreatedModified):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['-id']
        db_table = 'outcome_template'


class OutcomeTemplateDetail(CreatedModified):
    outcome = models.ForeignKey(
        "outcome.Outcome",
        on_delete=models.CASCADE,
        related_name="outcome_detail",

        null=True)

    outcome_template = models.ForeignKey(
        "outcome.OutcomeTemplate",
        related_name="outcome_template_detail",
        on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-id']
        db_table = 'outcome_template_details'
