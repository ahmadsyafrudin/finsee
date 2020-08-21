from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from finsee.utils.models import CreatedModified


class Income(CreatedModified):
    name = models.CharField(max_length=128)
    amount = models.DecimalField(
        decimal_places=2, max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))])

    period = models.CharField(max_length=25, choices=[
        ('monthly', 'monthly'),
        ('once', 'Once'),
        ('daily', 'Daily')
    ])

    class Meta:
        db_table = 'income'
        ordering = ['-id']
