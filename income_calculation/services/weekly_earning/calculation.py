from datetime import datetime

from jdatetime import date, timedelta

from income_calculation.repositories.query.weekly import get_all_weekly_earning
from income_calculation.dtos.base import (CourierResponse, UserResponse)
from income_calculation.dtos.weekly import WeeklyEarningResponse


def get_first_day_of_persian_weeks_in_range(start_date, end_date):
    first_days_of_weeks = []
    start_date = date.fromgregorian(year=start_date.year,
                                    month=start_date.month, day=start_date.day)
    end_date = date.fromgregorian(
        year=end_date.year, month=end_date.month, day=end_date.day)
    current_date = start_date

    while current_date <= end_date:
        days = current_date.weekday()
        start_of_week = current_date - timedelta(days=current_date.weekday())
        first_days_of_weeks.append(start_of_week.togregorian())
        current_date += timedelta(days=7)

    return first_days_of_weeks


def get_weekly_earning(from_date, to_date):
    response = []
    start_dates = get_first_day_of_persian_weeks_in_range(
        start_date=from_date, end_date=to_date)

    result = get_all_weekly_earning(start_dates=start_dates)

    for item in result:

        response.append(WeeklyEarningResponse(courier=CourierResponse(id=item.courier.id, user=UserResponse(
            id=item.courier.user.id, email=item.courier.user.email)), amount=item.amount, start_date=item.start_date).dict())

    return response if response else None
