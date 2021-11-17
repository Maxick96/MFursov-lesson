vyr = float(input('Введите сумму выручки = '))
izd = float(input('Введите сумму издеркжи = '))
sum = vyr - izd
if vyr > izd:
    rent = sum/vyr
    print('Сумма прибыли = ', sum, ' руб')
    print('Рентабельность выручки = ', rent)
    sotr = int(input('Сколько сотрудников работает в компании?: '))
    sumkomp = sum / sotr
    print('В компании работает сотрудников = ', sotr)
    print('Прибыль фирмы в расчёте на одного сотрудника = ', sumkomp, ' руб')

elif vyr <= izd:
    print('Прибыли нет! Сумма убытка = ', sum, 'руб. Учитесь зарабатывать! :')