from datetime import datetime

from django.db import transaction

from rest_framework.serializers import (
    Serializer, DecimalField, IntegerField, DateTimeField, ValidationError)

from income_calculation.services.daily_income.calculation import (
    save_income_item, calculate_daily_income, get_courier_info)


class IncomeItemSerializer(Serializer):
    courier = IntegerField(write_only=True, required=True)
    amount = DecimalField(write_only=True, required=True,
                          max_digits=10, decimal_places=2)

    @staticmethod
    def validate_courier(value):
        if not get_courier_info(courier_id=value):
            raise ValidationError('The courier is not valid')

        return value

    @transaction.atomic
    def create(self, validated_data):
        if result := save_income_item(courier_id=validated_data['courier'], amount=validated_data['amount']):
            return calculate_daily_income(courier_id=result['courier']['id'], date=result['date'])
