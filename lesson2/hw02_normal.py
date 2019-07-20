# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


import math




listA = [-32, 0, 1, 23, 29329, 4, 8, 9, 25, -31]
listB = []


for i in listA:
    if i >= 0 and math.sqrt(i) % 1 == 0:
        listB.append(int(math.sqrt(i)))

print(listB)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


days = {"01": "первое", "02": "второе", "03": "третье", "04": "четвертое", "05": "пятое", "06": "шестое",
        "07": "седьмое", "08": "восьмое", "09": "девятое", "10": "десятое", "11": "одинадцатое", "12": "двенадцатое",
        "13": "тринадцатое", "14": "четырнадцатое", "15": "пятнадцатое", "16": "шестнадцатое", "17": "семнадцатое",
        "18": "восемнадцатое", "19": "девятнадцатое", "20": "двадцатое", "21": "двадцать первое",
        "22": "двадцать второе",
        "23": "двадцать третье", "24": "двадцать четвертое", "25": "двадцать пятое", "26": "двадцать шестое",
        "27": "двадцать седьмое", "28": "двадцать восьмое", "29": "двадцать девятое", "30": "тридцатое",
        "31": "тридцать первое"}
months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
           "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}


userDate = input("Введите дату в формате dd.mm.yyyy : ")
print(days[userDate[0:2]],months[userDate[3:5]], userDate[6:], "года")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random




import random




userList = []


listLength = int(input ("Введите желаемое количество элементов списка: "))
while len(userList) < listLength:
    userList.append(random.randint(-100,100))

print("Ваш список случайных чисел: ", userList)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]




randomList = [-2,3,4,0,23,34,2,3,4,5,2,2,1,2,5,8,3,4,6,7]
uniqueList = set(randomList)
uniqueList2 = []




for n in randomList:
    if n not in randomList:
        uniqueList2.append(n)

for m in randomList:
    if randomList.count(m) == 1:
        uniqueList2.append(m)


print("Список без повторений: ", uniqueList)
print("Список только с уникальными значениями: ", uniqueList2)
