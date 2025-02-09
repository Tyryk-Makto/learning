start = int(input('Начало отрезка?: '))
finish = int(input('Конец отрезка?: '))
step = int(input('Введите шаг: '))
if step > 0:
    step = step *- 1
if start > finish:
    start, finish = finish, start
for x in range(finish, start -1, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print('В точке' , x, 'функция равна', y)

