#1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a=1
print(a)
b=a+5
print(b)
print(type(b))
a = None
b = a
print(b)
print(type(b))
a = int(input('Введите число: '))
b = a//3
print(b ** 3)
print(type(b))
number = input('Введите несколько чисел от 1 до 10 через запятую: ')
print(number)
print(type(number))
number = int(input('Введите число 0 <= name <= 100: '))
if number < 0:
    print('Вы ввели число, меньше нуля, нужно больше')
elif number > 100:
    print('Вы ввели число больше 100, нужно меньше')
else:
    number_new = number ** 0.5
    print(type(number_new))
    print(number_new)
#фантазия иссякла