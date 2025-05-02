from django.test import TestCase
from datetime import datetime, timedelta
from .models import YourModel  # Replace with your actual model

class DurationTestCase(TestCase):
    def setUp(self):
        # Set up any initial data for the tests
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2023, 12, 31)

    def test_duration_days(self):
        duration = (self.end_date - self.start_date).days
        self.assertEqual(duration, 364)

    def test_duration_weeks(self):
        duration_days = (self.end_date - self.start_date).days
        duration_weeks = duration_days // 7
        self.assertEqual(duration_weeks, 52)

    def test_duration_percentage(self):
        current_year_days = 365  # Adjust for leap years if necessary
        duration_days = (self.end_date - self.start_date).days
        duration_percentage = (duration_days / current_year_days) * 100
        self.assertAlmostEqual(duration_percentage, 99.45, places=2)  # Adjust based on actual calculation

    # Add more tests as needed for your application logic