sec = float(input('Введите кол-во секунд: '))
hour = sec//3600
sec %= 3600
minute = sec // 60
sec %= 60
print(f'Результат конвертации секунд - {int(hour)}:{int(minute)}:{int(sec)}')