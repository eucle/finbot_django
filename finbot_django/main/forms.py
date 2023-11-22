from django import forms


class DateForm(forms.Form):
    start_date = forms.DateField(
        label='Дата начала периода',
        help_text='Укажи дату начала',
        widget=forms.DateTimeInput(attrs={'type': 'date'})
    )

    end_date = forms.DateField(
        label='Дата окончания периода',
        help_text='Укажи дату окончания',
        widget=forms.DateTimeInput(attrs={'type': 'date'})
    )
