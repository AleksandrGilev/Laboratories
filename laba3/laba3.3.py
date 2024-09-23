from datetime import *

print('')
date_start = input('Введите дату и время отправления поезда в виде Месяц/День/Год Час:Минуты:')
print('Введите дату и время прибытия поезда в виде Месяц/День/Год Час:Минуты')
date_finish = input()

try:
    datetime_start = datetime.strptime(date_start, '%m/%d/%Y %H:%M')
    datetime_finish = datetime.strptime(date_finish, '%m/%d/%Y %H:%M')
    date = datetime_finish - datetime_start
    print('Время в пути:', date)
except:
    print('Введена неверная дата')