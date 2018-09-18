from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from utils.models import CreatedModified


class Income(CreatedModified):
    name = models.CharField(max_length=250)
    amount = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    income_type = models.CharField(max_length=25, choices=[
        ('salary', 'Salary'),
        ('profit', 'Profit'),
        ('other', 'Other')

    ])
