import math




a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
d= b**2 - 4*a*c

if d<0:
    print("Уравнение корней не имеет")
elif d==0:
    x = (-1*b)/2*a
    print ("Корень уравнения равен: ", x)
else:
    x1 = ((-1*b)+ math.sqrt(d))/2*a
    x2 = ((-1*b)- math.sqrt(d))/2*a
    print ("Первый корень уравнения равен: ",x1," Второй корень уравнения равен: ",x2)

