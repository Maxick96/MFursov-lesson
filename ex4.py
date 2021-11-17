chislo = int(input('Введите целое положительное число: '))
maxcifra = chislo % 10
chislo //= 10
while chislo > 0:
    if chislo % 10 > maxcifra:
        maxcifra = chislo % 10
    chislo //= 10
print('Максимальная цифра - ', maxcifra)