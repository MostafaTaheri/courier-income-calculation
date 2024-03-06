from income_calculation.models import (IncomeItem, DailyIncome)


def store_daily(courier_id, date, amount):
    if obj_ := DailyIncome.objects.filter(courier_id=courier_id, date=date).first():
        obj_.amount = amount
        obj_.save()
    else:
        obj_ = DailyIncome.objects.create(
            courier_id=courier_id, date=date, amount=amount)

    return obj_


def store_income_item(courier_id, date, amount):
    return IncomeItem.objects.create(courier_id=courier_id, amount=amount, date=date)
