### Dates ### 

from datetime import datetime, time, timedelta, date

now = datetime.now() # modela la fecha y hora actual

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

date_random = datetime(2023, 1, 1, 2, 3) # modela una fecha y hora especifica

print(date_random)

random_time = time(23, 22, 1) # Modela una Hora


print(random_time)

birthdate = date(2002, 10, 9) # Modela una fecha epecifica, para la fecha actual = date.today()

print(birthdate)
print(birthdate.year)
print(birthdate.month)
print(birthdate.day)


print(now- date_random) # Esto se puede hacer con  modulo importado de timedelta, dos objetos de tipo "datetime"

print(now.date() - birthdate) # dos objetos de tipo "date"