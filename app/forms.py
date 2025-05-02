from django import forms
from datetime import datetime

class DurationForm(forms.Form):
    start_date = forms.CharField(label="Start Date (dd/mm/yy)", required=True)
    end_date = forms.CharField(label="End Date (dd/mm/yy, optional)", required=False)
    include_today = forms.BooleanField(label='Inclure la date du jour', required=False)

    def clean_start_date(self):
        data = self.cleaned_data['start_date']
        try:
            return datetime.strptime(data, '%d/%m/%y').date()
        except ValueError:
            raise forms.ValidationError("Invalid start date format. Use dd/mm/yy.")

    def clean_end_date(self):
        data = self.cleaned_data.get('end_date')
        if data:
            try:
                return datetime.strptime(data, '%d/%m/%y').date()
            except ValueError:
                raise forms.ValidationError("Invalid end date format. Use dd/mm/yy.")
        return None
