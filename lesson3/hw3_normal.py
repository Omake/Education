# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachi(n, m):
    fibRow = [1, 1]
    while len(fibRow) < m:
        fibRow.append(fibRow[-1] + fibRow[-2])
    return (fibRow[n:m])


n = int(input("Введите с какого элемента выводить ряд: "))
m = int(input("Введите до какого элемента выводить ряд: "))
print(fibonachi(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print("После сортировки список выглядит следующим образом: ", sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filtration(*args):
    filteredList = []
    for arg in args:
        if type(arg) == int:
            filteredList.append(arg)
    return filteredList


print("Отфильтрованный список: ", filtration(2, 0, "vasya", "petya", False, 0.2, 5, 2, 123, "sobaka"))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


import math

A1 = (3, 10)
A2 = (12, 10)
A3 = (11, 5)
A4 = (2, 5)
B1 = (3, 123)
B2 = (12, 10)
B3 = (11, 5)
B4 = (2, 5)


def lenByCord(A, B):
    # Решил сделать отдельную функцию для рассчета длин сторон
    return abs(math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2))


def parallelogramCheck(A, B, C, D):
    if lenByCord(A, B) == lenByCord(C, D) and lenByCord(A, D) == lenByCord(B, C):
        return print("Вершины образуют паралеллограмм")
    else:
        return print("Вершины не образуют паралеллограмм")


parallelogramCheck(A1, A2, A3, A4)
parallelogramCheck(B1, B2, B3, B4)
