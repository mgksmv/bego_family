from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    date = forms.DateField(label='Дата', widget=DateInput())
