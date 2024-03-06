from django.urls import path

from income_calculation.apis.views.daily import IncomeItemAPIView
from income_calculation.apis.views.weekly import WeeklyEarningAPIView


urlpatterns = [
    path('income-item/', IncomeItemAPIView.as_view(), name='income-item'),
    path('weekly/', WeeklyEarningAPIView.as_view(), name='weekly'),
]
