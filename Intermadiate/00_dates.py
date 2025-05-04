# Dates

from datetime import datetime, time, date, timedelta

now = datetime.now()

timestamp = now.timestamp() # 1746240111.06862 / Representación única de tiempo
print(timestamp)

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print_date(year_2023)
print_date(datetime(2023, 10, 15, 13))

current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# operaciones con fechas

current_date = date.today()
print(current_date)
print(current_date + timedelta(days=1)) # suma 1 día
print(current_date + timedelta(days=7)) # suma 7 días
print(current_date + timedelta(weeks=1)) # suma 1 semana
print(current_date + timedelta(weeks=2)) # suma 2 semanas
print(current_date + timedelta(weeks=3)) # suma 3 semanas

diff = current_date - now.date() # diferencia entre fechas
print(diff.days) # diferencia en días

start_timedelta = timedelta(days=1, hours=2, minutes=3, seconds=4) # diferencia de tiempo
end_timedelta = timedelta(days=2, hours=3, minutes=4, seconds=5) # diferencia de tiempo
print(end_timedelta - start_timedelta) # diferencia entre tiempos
print(start_timedelta + end_timedelta) # suma de tiempos

# un timedelta es una diferencia de tiempo, no una fecha
# Podemos sumar un timedelta a una fecha para obtener una nueva fecha
print(current_date + start_timedelta) # suma de fecha y tiempo