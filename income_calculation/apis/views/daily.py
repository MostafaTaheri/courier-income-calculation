import datetime

# from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED)

from income_calculation.apis.serializers.daily import IncomeItemSerializer


class IncomeItemAPIView(CreateAPIView):
    serializer_class = IncomeItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.save(), status=HTTP_201_CREATED)
