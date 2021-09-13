#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = (input('Введите целое, положительное число: '))
print(number)
#на память пришла функция max, из подготовительного курса
number_max = max(number)
print('Самая большая цифра в введённом числе: ',number_max)

#с помощью цикла for
numbers = (input('Введите целое, положительное число: '))
print(numbers)
number_max = 0
#переведём строчный формат в числовой
numbers = [int(number) for number in numbers]
print(numbers)
for number in numbers:
	if number > number_max:
		number_max = number
print('Самая большая цифра в ведённом числе: ', number_max)

#с помощью цикла while
numbers = (input('Введите целое, положительное число: '))
print(numbers)
#переведём строчный формат в числовой
#numbers = [int(number) for number in numbers]
#print(numbers)
n = len(numbers)
print(n)
i = 0
number_max = 0
while i < n:
	number = int(numbers[i])
	if number_max < number:
		number_max = number
	i += 1
print('Самая большая цифра в введённом числе: ',number_max)

