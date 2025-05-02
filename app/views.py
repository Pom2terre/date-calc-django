from django.shortcuts import render, redirect
from .forms import DurationForm
from datetime import datetime

def home(request):
    return redirect('calculate-duration')

def calculate_duration(request):
    context = {}
    if request.method == 'POST':
        form = DurationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date'] or datetime.today().date()
            delta = end_date - start_date
            days = delta.days
            context.update({
                'start_date': start_date.strftime('%d/%m/%y'),
                'end_date': end_date.strftime('%d/%m/%y'),
                'time_duration_days': days,
                'time_duration_months': days // 30,
                'time_duration_remaining_days_in_month': days % 30,
                'time_duration_seconds': days * 86400,
                'time_duration_minutes': days * 1440,
                'time_duration_hours': days * 24,
                'time_duration_weeks': round(days / 7, 2),
                'time_duration_percentage': round(days / 365 * 100, 2),
                'current_year': end_date.year,
            })
            context['calculation_done'] = True
        else:
            context['form'] = form
    else:
        form = DurationForm()
        context['form'] = form
    return render(request, 'calculate_duration.html', context)