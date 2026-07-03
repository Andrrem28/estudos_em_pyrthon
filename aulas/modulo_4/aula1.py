# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

# date_str_data = '01-07-2026 08:20:30'
# date_str_fmt = '%d-%m-%Y %H:%M:%S'
# date = datetime(2026, 7, 1)
# date_whit_datetime = datetime(2026, 7, 1, 8, 20, 30)
# date_with_strptime = datetime.strptime(date_str_data, date_str_fmt, tzinfo=timezone('America/Fortaleza'))
# print(date.now())
# print(date)
# print(date_whit_datetime)
# print(date_with_strptime)

# date = datetime.now(timezone('America/Fortaleza'))
date = datetime.now()

print(date.timestamp())
print(datetime.fromtimestamp(date.timestamp()))
