# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math


class Tri:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        print(f"Координаты вершин треугольника: \n A: {self.a} \n B: {self.b} \n C: {self.c}")

    def square(self):
        return abs(
            (self.b[0] - self.a[0]) * (self.c[1] - self.a[1]) - (self.c[0] - self.a[0]) * (self.b[1] - self.a[1])) / 2

    def perimeter(self):
        return abs(math.sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)) + abs(
            math.sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)) + abs(
            math.sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2))

    def height(self):
        # Реализовал функцию для вычисления высоты только для одного угла А из-за экономии времени.
        return abs(
            abs((self.b[1] - self.c[1]) * self.a[0] + (self.c[0] - self.b[0]) * self.a[1] + (self.b[0] * self.c[1]
                                                                                             - self.c[0] * self.b[
                                                                                                 1])) / (
                math.sqrt((self.b[1] - self.c[1]) ** 2 + (self.c[0] - self.b[0]) ** 2)))


triABC = Tri([0, 0], [0, 5], [3, 0])

print(f"Высота из вершины A равна: {triABC.height()}")
print(f"Периметр треугольника ABC равен: {triABC.perimeter()}")
print(f"Площадь треугольника ABC равна: {triABC.square()}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trap:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def sideLen(self, dot1, dot2):
        return math.sqrt((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2)

    def itsATrap(self):
        return  self.sideLen(self.a,self.d) == self.sideLen(self.b,self.c) and self.a[1] - self.d[1] == self.b[1]-self.c[1]


    def perimeter(self):
        return self.sideLen(self.a,self.b) + self.sideLen(self.b,self.c)+ self.sideLen(self.c,self.d) + self.sideLen(self.d,self.a)

    def square(self):
        h = math.sqrt((self.sideLen(self.d,self.a)**2 - (self.d[0]-self.a[1])**2))
        return h*(self.sideLen(self.a,self.b)+self.sideLen(self.c,self.d))/2

trapABCD = Trap([2,5],[7,5],[8,1],[1,1])
print(f"Длинна стороны AB: {trapABCD.sideLen(trapABCD.a,trapABCD.b)}\n"
      f"Длинна стороны BC: {trapABCD.sideLen(trapABCD.b,trapABCD.c)}\n"
      f"Длинна стороны CD: {trapABCD.sideLen(trapABCD.c,trapABCD.d)}\n"
      f"Длинна стороны AD: {trapABCD.sideLen(trapABCD.a,trapABCD.d)}")
print("Это равнобочная трапеция? ",trapABCD.itsATrap())
print("Периметр трапеции равен: ",trapABCD.perimeter())
print("Площадь трапеции равна: ",trapABCD.square())