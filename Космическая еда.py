buckwheat = int(input('Сколько килиграмм гречки?: '))
month_m = 1
for g in range(buckwheat -4, -1, -4):
    print('Через', month_m,'месяц: ', g, 'кг гречки в запасе.')
    month_m += 1
print()
print('Запасы закончились!')