from decimal import Decimal
from datetime import datetime

from income_calculation.dtos.base import (CourierResponse, BaseModel)


class WeeklyEarningResponse(BaseModel):
    courier: CourierResponse
    amount: Decimal
    start_date: datetime
