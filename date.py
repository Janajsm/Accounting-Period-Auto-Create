//Auto Created Weekly
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

//Auto Created Monthly
from datetime import timedelta
import pandas as pd

date_len=pd.date_range(start='2024-01-01',end='2024-12-31',freq='MS')
# print(date_len)
for i in date_len:
        start_date=i
        # print(i)
        ed_date = start_date + timedelta(days=32)
        # print(ed_date)
        end_date = ed_date.replace(day=1) - timedelta(days=1)
        # print(end_date)
        period_name=end_date.strftime("%B-%Y")
        print(period_name)
        print(start_date.strftime("%Y-%m-%d"))
        print(end_date.strftime("%Y-%m-%d"))












