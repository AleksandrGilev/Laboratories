import datetime

date_start = input('Введите дату и время отправления поезда в виде Месяц/День/Год Час:Минуты:')
date_finish = input('Введите дату и время прибытия поезда в виде Месяц/День/Год Час:Минуты:')

try:
    datetime_start = datetime.strptime(date_start, '%m/%d/%Y %H:%M')
    datetime_finish = datetime.strptime(date_finish, '%m/%d/%Y %H:%M')
except ValueError:
    print('Введена неверная дата')

date = datetime_finish - datetime_start
print('Время в пути:', date)
