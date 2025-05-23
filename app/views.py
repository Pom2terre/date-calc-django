from django.shortcuts import render, redirect
from .forms import DurationForm
from datetime import datetime, timedelta
import os
from django.conf import settings

def home(request):
    return redirect('calculate-duration')

def calculate_duration(request):
    context = {}
    if request.method == 'POST':
        form = DurationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            include_today = form.cleaned_data.get('include_today', False)
            end_date = form.cleaned_data['end_date'] or datetime.today().date()
            # ➕ Si on inclut la date du jour, on ajoute 1 jour
            if include_today:
                delta = end_date - start_date + timedelta(days=1)
            else:
                delta = end_date - start_date
            # ➕ Si la date de fin est inférieure à la date de début, on inverse les dates
            if delta.days < 0:
                start_date, end_date = end_date, start_date
                delta = end_date - start_date
            # ➕ On calcule la durée en jours
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
                'calculation_done': True,
                'include_today': include_today,
            })
        else:
            context['form'] = form
    else:
        form = DurationForm()
        context['form'] = form

    # ✅ Toujours définir ces deux variables
    context['environment'] = os.getenv("DJANGO_ENV", "dev")
    context['debug'] = settings.DEBUG

    # ✅ Version de l'application
    # Assurez-vous que APP_VERSION est défini dans vos settings.py
    context['app_version'] = settings.APP_VERSION


    return render(request, 'calculate_duration.html', context)