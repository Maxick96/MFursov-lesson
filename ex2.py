sec = float(input('Введите количество секунд: '))
hour = sec//3600
sec %= 3600
minute = sec // 60
sec %= 60
print(f'Результат конвертации секунд (чч:мм:сек) - {int(hour)}:{int(minute)}:{int(sec)}')