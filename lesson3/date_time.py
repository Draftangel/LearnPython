from datetime import date, timedelta, datetime

today = date.today()
print("Сегодня: " + today.strftime("%Y/%m/%d"))

yesterday = today - timedelta(days=1)
print("Вчера было: " + yesterday.strftime("%Y/%m/%d"))

month_ago = today - timedelta(days=30)
print("30 дней назад было: " + month_ago.strftime("%Y/%m/%d"))

dt_string = "01/01/25 12:10:03.234567"
dt = datetime.strptime(dt_string, '%d/%m/%y %H:%M:%S.%f')
print(f'Строка {dt_string} превращена в объект {type(dt)} со значением {dt}')

