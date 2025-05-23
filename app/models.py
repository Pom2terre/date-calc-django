from django.db import models

class Duration(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def calculate_duration(self):
        return (self.end_date - self.start_date).days

    def __str__(self):
        return f"Duration from {self.start_date} to {self.end_date}"