#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time = int(input('Введите время в секундах: '))
print(time)
#определим количество часов в введённом числе
hour = time // 3600
print(hour)
#определим количество минут за рамками полного часа в ведённом числе
minute = (time - (hour*3600)) // 60
print(minute)
#определим количество оставшихся секунд в ведённом числе
second = time - (hour*3600) - (minute*60)
print(second)
#итак, мы получили искомые величины, осталось собрать их красиво, воспользовавшись методом форматирования
if hour < 10:
    hour = '0' + str(hour)
else:
    hour = str(hour)
if minute < 10:
    minute = '0' + str(minute)
else:
    minute = str(minute)
if second < 10:
    second = '0' + str(second)
else:
    second = str(second)
time = hour + ':' + minute + ':' + second
print(time)
time = '%s:%s:%s'%(hour, minute, second)
print(time)
time = '{}:{}:{}'.format(hour, minute, second)
print(time)
time = f'{hour}:{minute}:{second}'
print(time)
#для проверки введём 2 числа: первое - 3965, проверим плавающие нули,
#затем, какое-то большое число, посмотрим, как работают часы
#молодец:) всё крутится...