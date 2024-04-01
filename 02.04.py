from datetime import datetime as dt
now = dt.now()
from datetime import date
date = date.today()
time = dt.now().time()
today = dt.today().weekday()
week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
print('Сегодня', week[today], 'сейчас', time, 'дата:', date)
