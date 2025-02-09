number_debtors = int(input('Сколько должников?: '))
summ = 0
for p in range(0, number_debtors, 5):
    print('Должник с номером', p)
    debt = int(input('Сколько должны?: '))
    summ += debt
    print()
print('Общая сумма долга:', summ)