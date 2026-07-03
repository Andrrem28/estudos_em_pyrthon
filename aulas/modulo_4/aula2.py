# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('01/07/2026 08:20:30', fmt)
data_fim = datetime.strptime('02/03/2024 08:20:30', fmt)

delta = relativedelta(days=10, hours=5, minutes=30)

# delta = timedelta(days=10, hours=5, minutes=30)
# delta = data_inicio - data_fim

print(delta)
print(data_fim)
print(data_fim + relativedelta(years=2, months=3, days=10, hours=5, minutes=30))

# print(data_fim - delta)
# print(delta.days, delta.seconds, delta.total_seconds())
# print(data_inicio > data_fim)
# print(data_inicio < data_fim)
# print(data_inicio == data_fim)