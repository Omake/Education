"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random

"""
def getBarrelFromPool():
    n = random.randrange(len(pool))
    print(f"Достали боченок с номером {pool[n]}")
    pool.pop(n)

playerPool = []
while len(playerPool) < 15:
"""


# pool = [i for i in range(1, 11)]

class Pool(list):
    def refill(self):
        self.clear()
        for i in range(1, 91):
            self.append(i)

    def roll(self):
        n = random.randrange(len(self))
        # print(f"Достали боченок с номером {self[n]}")
        currentBarrel = self[n]
        self.pop(n)

        return currentBarrel


class PlayerPool(Pool):
    def __init__(self, name):
        super().__init__(self)
        self.ticket = []
        self.name = name
        self.winCounter = 0

    def generateTicket(self):
        self.ticket = []
        while len(self) < 15:
            n = random.randrange(1, 91)
            if n not in self:
                self.append(n)
        self.ticket.append(sorted(self[0:5]))
        self.ticket.append(sorted(self[5:10]))
        self.ticket.append(sorted(self[10:15]))

        for i in range(0, 3):
            for _ in range(0, 4):
                self.ticket[i].insert(random.randint(0, len(self.ticket[i])), " ")

        return self.ticket

    def __str__(self):
        return f"Билет игрока {self.name}: \n{self.ticket[0]}\n{self.ticket[1]}\n{self.ticket[2]}\n\n"

    def playerPoolCheck(self, barrel):
        checker = False
        for i in self.ticket:
            for j in range(len(i)):
                if i[j] == barrel:
                    i[j] = "+"
                    checker = True
                    self.winCounter += 1
                    break
        return checker

        # if checker == False:
        #     return checker
        # else:
        #     return print(f"У игрока есть цифра {barrel}")
    def computerPoolCheck(self, barrel):
        checker = False
        for i in self.ticket:
            for j in range(len(i)):
                if i[j] == barrel:
                    i[j] = "+"
                    checker = True
                    self.winCounter += 1
                    break
        # if checker == False:
        #     pass
        # else:
        #     return print(f"У игрока {self.name} есть цифра {barrel}")
        if checker == True:
            print(f"Игрок {playerPool2.name} зачеркнул число {barrel} !!!")



mainPool = Pool()
mainPool.refill()
playerPool1 = PlayerPool("Кирилл")
playerPool2 = PlayerPool("Компьютер")
playerPool1.generateTicket()
playerPool2.generateTicket()

while True:
    if playerPool2.winCounter == 15:
        print(f"Игрок {playerPool2.name} победил!!!")
        break
    elif playerPool1.winCounter == 15:
        print(f"Игрок {playerPool1.name} победил!!!")
        break
    else:
        thisBarrel = mainPool.roll()
        print(playerPool1)
        print(playerPool2)
        answer = input(f"У тебя есть число {thisBarrel} ? (y/n): ")
        if answer == "y":
            if playerPool1.playerPoolCheck(thisBarrel) == True:
                print(f"Игрок {playerPool1.name} зачеркнул число {thisBarrel} !!!")
            else:
                print(f"Игрок {playerPool1.name} ошибся!!!")
                playerPool2.winCounter = 15
        elif answer == "n":
            if playerPool1.playerPoolCheck(thisBarrel) == True:
                print(f"Игрок {playerPool1.name} ошибся!!!")
                playerPool2.winCounter = 15
            else:
                pass
        else:
            print("Очень жаль, но вы не смогли ответить на простой вопрос y/n и испортили игру. Всего доброго.")
            break
        playerPool2.computerPoolCheck(thisBarrel)


