# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class Person:
    def __init__(self, name, classRoom):
        self.name = name
        self.classRoom = classRoom



class Teacher(Person):
    def __init__(self, name, subject, classRoom):
        super().__init__(name, classRoom)
        self.subject = subject

    def teacherByClassroom(classRoom, teachers):
        teachersByClassroom = []
        for teacher in teachers:
            if classRoom in teacher.classRoom:
                teachersByClassroom.append(teacher.name)
        return teachersByClassroom


class Student(Person):
    def __init__(self, name, classRoom, mother, father):
        super().__init__(name, classRoom)
        self.mother = mother
        self.father = father

    def getStudentsByClassRoom(classRoom, students):
        studentsList = []
        for person in students:
            if classRoom in person.classRoom:
                studentsList.append(person.name)
            studentsList = ['{} {:.1}. {:.1}.'.format(*n.split()) for n in studentsList]
        return studentsList

    def checkSubjects(self, teachers):
        studentsSubjects = []
        for teacher in teachers:
            if self.classRoom[0] in teacher.classRoom:
                studentsSubjects.append(teacher.subject)
        return studentsSubjects

    def getStudentsParents(self):
        return self.mother, self.father


students = [Student("Пупкин Василий Васильевич", ["5Г"], "Пупкина Василиса Павловна", "Пупкин Василий Леонидович"),
            Student("Петров Петр Петрович", ["5Г"], "Петрова Елена Петровна", "Петров Иван Петрович"),
            Student("Иванов Кирилл Иванович", ["8Б"], "Иванова Елена Владимировна", "Иванов Иван Васильевич")
            ]
teachers = [Teacher("Светлана Иванова", "Алгебра", ["5Г", "7А", "8В"]),
            Teacher("Сергей Жуков", "Геометрия", ["7У", "8В", "5Г"])
            ]


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

def merge(lst, res=[]):
    # Честно своровал эту функцию, чтобы объеденять вложенные списки в один
    for el in lst:
        merge(el) if isinstance(el, list) else res.append(el)
    return res

def getClassRoomList():
    classRoomList = []
    for person in students:
        classRoomList.append(person.classRoom)
    for person in teachers:
        classRoomList.append(person.classRoom)
    return set(merge(classRoomList))


print("Список классов: ", getClassRoomList())
print("Ученики в заданном классе: ", Student.getStudentsByClassRoom("5Г",students))
print("Родители ученика: ",Student.getStudentsParents(students[1]))
print("Предметы ученика: ",Student.checkSubjects(students[0], teachers))
print("Учителя, преподающие в классе: ",Teacher.teacherByClassroom("8В", teachers))