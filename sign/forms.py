from django import forms

from django.forms import DateField


class ZodiacForm(forms.Form):
    day = forms.IntegerField(max_value=31, min_value=1, label='day')
    month = forms.CharField(max_length=20, label='Month')


class ZodiacForm2(forms.Form):
    birthdate = DateField(widget=forms.SelectDateWidget())
