from django import forms
from App_Keyword.models import KeywordSearch


class TimeDurationForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()

