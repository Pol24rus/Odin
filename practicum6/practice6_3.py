"""Принимает текущую дату и время"""
"""Вычисляет кол-во дней в году"""
"""Находит разницу между 2мя заданными датами"""
import datetime

def get_current_datetime():
    return datetime.datetime.now()


def days_intil_holiday(holiday_date):
    current_date = get_current_datetime().date()
    # delta = holiday_date - current_date
    delta = diiference_between_dates(holiday_date, current_date)
    return delta.days


def diiference_between_dates(date1, date2):
    return abs((date2 - date1).days)


def main():
    today = get_current_datetime()
    new_year = datetime.date(today.year, 12, 31)
    print(f"Дней до нового года: {days_intil_holiday(new_year)}")

    date1 = datetime.date(2024, 10, 1)
    date2 = datetime.date(2025, 5, 4)
    print(f"Разница между {date1} и {date2} составляет {diiference_between_dates(date1, date2)}")

main()