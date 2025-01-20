number=int(input('Введите четырехзначное число: '))
number1=number//1000
number2=number%1000//100
number3=number%100//10
number4=number%10
print('Цифры числа: ', number1, number2, number3, number4)

