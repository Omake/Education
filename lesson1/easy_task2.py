data1 = input("Введите первую переменную: ")
data2 = input("Введите вторую переменную: ")

buffer = data1

data1 = data2

data2 = buffer

print ("Теперь первая переменная равна: ",data1," Теперь вторая переменная равна: ",data2)