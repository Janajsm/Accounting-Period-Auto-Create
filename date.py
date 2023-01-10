
from datetime import timedelta
import pandas as pd

name='Tuesday'
wk_name='W'+'-'+name[0:3]
# print(wk_name)
date_len=pd.date_range(start='2022-12-26',end='2024-02-01',freq=wk_name)
# print(date_len)
for i in date_len:
    # if i.date().strftime("%A")=="Friday":
        start_date=i
        end_date=start_date+timedelta(days=6)
        period_name2=end_date.strftime("%U-Week %Y")
        print(period_name2)
        print(start_date.strftime("%Y-%m-%d"))
        print(end_date.strftime("%Y-%m-%d"))




""" Given Year get month Start date and End date """
'''
from datetime import datetime, timedelta

def get_month_start_end(year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date + timedelta(days=32)
    print(end_date)
    end_date = end_date.replace(day=1) - timedelta(days=1)
    return (start_date, end_date)

# Example usage
year = 2020
month = 2
start_date, end_date = get_month_start_end(year, month)
print(f'Start date: {start_date.strftime("%Y-%m-%d")}')
print(f'End date: {end_date.strftime("%Y-%m-%d")}')'''

'''
from datetime import datetime, timedelta

def get_month_start_end(year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date + timedelta(days=32)
    end_date = end_date.replace(day=1) - timedelta(days=1)
    return (start_date, end_date)

def get_year_month_ranges(year):
    month_ranges = []
    for month in range(1, 13):
        start_date, end_date = get_month_start_end(year, month)
        month_ranges.append((start_date, end_date))
    return month_ranges

# Example usage
year = 2020
month_ranges = get_year_month_ranges(year)
for start_date, end_date in month_ranges:
    print(f'Start date: {start_date.strftime("%Y-%m-%d")}')
    print(f'End date: {end_date.strftime("%Y-%m-%d")}')'''

# from datetime import datetime, timedelta

# def get_month_start_end(year, month):
#     start_date = datetime(year, month, 1)
#     end_date = start_date + timedelta(days=32)
#     end_date = end_date.replace(day=1) - timedelta(days=1)
#     return (start_date, end_date)

# def get_date_range_month_ranges(start_date, end_date):
#     month_ranges = []
#     current_date = start_date
#     while current_date <= end_date:
#         start_date, end_date = get_month_start_end(current_date.year, current_date.month)
#         month_ranges.append((start_date, end_date))
#         current_date = end_date + timedelta(days=1)
#     return month_ranges

# # Example usage
# start_date = datetime(2020, 1, 1)
# end_date = datetime(2020, 12, 31)
# month_ranges = get_date_range_month_ranges(start_date, end_date)
# for start_date, end_date in month_ranges:
#     print(f'Start date: {start_date.strftime("%Y-%m-%d")}')
#     print(f'End date: {end_date.strftime("%Y-%m-%d")}')










