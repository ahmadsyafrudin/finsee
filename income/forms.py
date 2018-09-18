from django.forms import ModelForm

from income.models import Income


class IncomeForm(ModelForm):

    class Meta:
        model = Income
        exclude = ['created', 'modified']
