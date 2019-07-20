"""matrix = [1,2,3], [4,5,6], [7,8,9]

for i, line in enumerate(matrix):
    for j, el in enumerate(line):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

print(list(map(list, zip(*matrix))))


keys = "aksjdkasjasdsadsadsadsadd"
values = range(10)
dict_g = {key: value for key, value in zip(keys, values)}
print(dict_g)

dict_g_2 = {el: el+4 for el in [1,2,3,4,5,6,7,2,312,22,32,32323]}
print(dict_g_2)


import re




string = "This is a simple test message for test"
string2 = "test"
pattern1 = "test"
pattern2 = "^test"
pattern3 = "^test$"

print(re.search(pattern1, string) is None)




import re

string = "this is a test"
found = re.findall(r"tes2t",string)
print(found)
"""


f = open("1.txt")
ints = []

try:
    for line in f:
        ints.append((int(line)))
except ValueError:
    print("Это не число")
except Exception:
    print ("Неизвестное значение")
else:
    print("Всё ок")
finally:
    f.close()
    print("Файлик закрыт")