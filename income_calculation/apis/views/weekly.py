from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.serializers import ValidationError

from income_calculation.services.weekly_earning.calculation import get_weekly_earning


class WeeklyEarningAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        s = self.kwargs
        if not self.request.query_params.get('from_date'):
            raise ValidationError({'from_date': 'This field is required'})

        if not self.request.query_params.get('to_date'):
            raise ValidationError({'to_date': 'This field is required'})

        try:
            from_date = datetime.strptime(
                self.request.query_params.get('from_date'), "%Y-%m-%d").date()
            to_date = datetime.strptime(
                self.request.query_params.get('to_date'), "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError('Invalid date format. use `%Y-%m-%d` ')

        response = get_weekly_earning(from_date=from_date, to_date=to_date)

        return Response(data=response, status=HTTP_200_OK)
