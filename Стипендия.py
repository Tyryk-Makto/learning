educational_grant = int(input('Ежемесячная стипендия?: '))
expenses  = int(input('Расходы в месяц?: '))
exx = expenses
month = 1
summ = 0
for x in range(1, 10 +1, 1):
    print(month, '-й месяц: траты', expenses, 'рублей, не хватает', summ, 'рублей.')
    up_money = int((exx * 0.03) + exx - educational_grant)
    month += 1
    summ += up_money
print()
print('Сумма денег, которую необходимо получить у родителей:',summ, 'рублей.')
