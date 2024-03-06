from django.db import models
from django.contrib.auth.models import User


class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class IncomeItem(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()


class DailyIncome(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class WeeklyEarning(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()

    class Meta:
        unique_together = ('courier', 'start_date')
