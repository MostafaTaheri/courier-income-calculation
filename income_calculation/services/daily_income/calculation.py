from datetime import datetime

from income_calculation.repositories.command.daily import (
    store_daily, store_income_item)
from income_calculation.repositories.query.daily import (
    get_income_items, get_total_amount_income_items, get_courier)
from income_calculation.dtos.daily import (
    DailyIncomeResponse, IncomeItemResponse)
from income_calculation.dtos.base import (UserResponse, CourierResponse)


def calculate_daily_income(courier_id, date):
    date = date.date()

    daily_income = get_total_amount_income_items(
        courier_id=courier_id, date=date)

    result = store_daily(courier_id=courier_id, date=date, amount=daily_income)
    response = DailyIncomeResponse(courier=CourierResponse(id=result.courier.id, user=UserResponse(
        id=result.courier.user.id, email=result.courier.user.email)), amount=result.amount, date=result.date)

    return response.dict()


def save_income_item(courier_id, amount):
    if result := store_income_item(
            courier_id=courier_id, amount=amount, date=datetime.now()):
        return IncomeItemResponse(courier=CourierResponse(id=result.courier.id, user=UserResponse(
            id=result.courier.user.id, email=result.courier.user.email)), amount=result.amount, date=result.date).dict()

    return None


def get_courier_info(courier_id):
    if result := get_courier(courier_id=courier_id):
        return CourierResponse(id=result.id, user=UserResponse(
            id=result.user.id, email=result.user.email))
    else:
        return None
