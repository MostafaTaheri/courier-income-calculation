from decimal import Decimal
from datetime import datetime

from income_calculation.dtos.base import (BaseModel, CourierResponse)


class DailyIncomeResponse(BaseModel):
    courier: CourierResponse
    amount: Decimal
    date: datetime


class IncomeItemResponse(BaseModel):
    courier: CourierResponse
    amount: Decimal
    date: datetime
