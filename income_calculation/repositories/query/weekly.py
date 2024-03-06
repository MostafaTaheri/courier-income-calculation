from income_calculation.models import WeeklyEarning


def get_all_weekly_earning(start_dates):
    return WeeklyEarning.objects.filter(start_date__in=start_dates)
