#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#напишем скрипт, используя словарь
month = int(input('Введите наименование месяца от 1 до 12: '))
month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
print('Наш месяц: ', month_dict[month])
season = {}
season.update(dict.fromkeys([12, 1, 2], 'зима'))
season.update(dict.fromkeys([3, 4, 5], 'весна'))
season.update(dict.fromkeys([6, 7, 8], 'лето'))
season.update(dict.fromkeys([9, 10, 11], 'осень'))
print('Время года: ', season[month])
#кружит нормально, теперь перейдём к списку

#здесь обращаемся к модулю строки в поисках значения, посему, из вводимого вычитаем 1
month = int(input('Введите наименование месяца от 1 до 12: '))
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
print('Наш месяц: ', month_list[month-1])
season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print('Время года: ', season_list[month-1])
#как-то хлопотно, но работает... двигаемся дальше