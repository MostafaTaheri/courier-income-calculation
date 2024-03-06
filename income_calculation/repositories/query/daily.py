from datetime import datetime

from django.db.models import Sum

from income_calculation.models import (IncomeItem, DailyIncome, Courier)


def get_income_items(courier_id, date):
    return IncomeItem.objects.filter(courier_id=courier_id, date=date)


def get_total_amount_income_items(courier_id, date):
    items = IncomeItem.objects.filter(courier_id=courier_id, date__date=date)
    return items.aggregate(Sum('amount'))['amount__sum'] or 0


def get_courier(courier_id):
    try:
        return Courier.objects.get(pk=courier_id)
    except:
        return None
