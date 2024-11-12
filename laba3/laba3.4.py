from datetime import *

date_birth = input('Введите дату рождения в виде Month/Day/Year:')

try:
    date_birth = datetime.strptime(date_birth, '%m/%d/%Y')
except ValueError:
    print('Введена неверная дата')
    exit()

date_birth_10kd = date_birth + timedelta(days=10 ** 4)
print('10 000 дней вам исполнится', date_birth_10kd)
date_birth_1kkm = date_birth + timedelta(minutes=10 ** 6)
print('1 000 000 минут вам исполнится', date_birth_1kkm)
date_birth_1kkks = date_birth + timedelta(seconds=10 ** 9)
print('1 000 000 000 секунд вам исполнится', date_birth_1kkks)
