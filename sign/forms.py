from django import forms

from datetime import date

from .models import Person


class ZodiacForm(forms.Form):
    day = forms.IntegerField(max_value=31, min_value=1, label='day')
    month = forms.CharField(max_length=20, label='Month')


class PersonForm(forms.ModelForm):
    birthdate = forms.DateField(label="Birthdate MM/DD/YYYY", input_formats=["%m/%d/%Y", "%m-%d-%Y", "%m%d%Y"])
    class Meta:
        model = Person
        fields = ["birthdate"]
    #birthdate = DateField(widget=forms.SelectDateWidget())
