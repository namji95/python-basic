from datetime import datetime, timedelta

# for i in range(10, 1, -1):

now_date = datetime.now()
now_day = now_date.strftime('%d')
for i in range(int(now_day) - 19, 0, -1):
    mimus_date = now_date - timedelta(days=i)
    format_date = mimus_date.strftime('%Y%m%d')
    print(format_date)