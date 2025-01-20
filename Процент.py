summ = int(input('Сколько денег?: '))
doorstep = int(input('До какой суммы?: '))
percent = int(input('Какой процент?: '))
total_y = 0
while summ < doorstep:
    total_y += 1
    print(f'{total_y} год. {int(summ)} + {percent}% = {int(summ + summ *(percent/100))}')
    summ = summ + summ * (percent / 100)
print('Количество лет для достижения порога:', total_y)
