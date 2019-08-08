class Field:
    def __init__(self):
        self.body = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.filled = []

    def turn(self, cord, sign):
        if type(cord) == int and cord > 0 and cord < 10 and cord not in self.filled:
            if cord == 1:
                self.body[0][0] = sign
                self.filled.append(cord)
            elif cord == 2:
                self.body[0][1] = sign
                self.filled.append(cord)
            elif cord == 3:
                self.body[0][2] = sign
                self.filled.append(cord)
            elif cord == 4:
                self.body[1][0] = sign
                self.filled.append(cord)
            elif cord == 5:
                self.body[1][1] = sign
                self.filled.append(cord)
            elif cord == 6:
                self.body[1][2] = sign
                self.filled.append(cord)
            elif cord == 7:
                self.body[2][0] = sign
                self.filled.append(cord)
            elif cord == 8:
                self.body[2][1] = sign
                self.filled.append(cord)
            elif cord == 9:
                self.body[2][2] = sign
                self.filled.append(cord)
        else:
            return False

    def __str__(self):
        return f"Введите номер ячейки куда поставить знак: \
        \n{self.body[0]}\n\n{self.body[1]}\n\n{self.body[2]}"

    # Возвращает True в случае победы
    def winChecker(self):
        if (self.body[0][0] == self.body[0][1] and self.body[0][0] == self.body[0][2]) or (
                self.body[1][0] == self.body[1][1] and self.body[1][0] == self.body[1][2]) or (
                self.body[2][0] == self.body[2][1] and self.body[2][0] == self.body[2][2]) or (
                self.body[0][0] == self.body[1][0] and self.body[0][0] == self.body[2][0]) or (
                self.body[0][1] == self.body[1][1] and self.body[0][1] == self.body[2][1]) or (
                self.body[0][2] == self.body[1][2] and self.body[0][2] == self.body[2][2]) or (
                self.body[0][0] == self.body[1][1] and self.body[0][0] == self.body[2][2]) or (
                self.body[0][2] == self.body[1][1] and self.body[0][2] == self.body[2][0]):
            return True
        else:
            return False


class Player:
    def __init__(self, sign, name):
        self.sign = sign
        self.name = name


player1 = Player("X", "ВАСЯ")
player2 = Player("O", "ПЕТЯ")
field1 = Field()
activePlayer = player1


def gameStart(field, player):
    field.turn(int(input(f"Ходит {player.name}!!! Куда поставить {player.sign} ?")), player.sign)


while True:
    if activePlayer == player1:
        print(field1)
        if field1.winChecker() == True:
            print(activePlayer.name, "Победил!!!")
            break
        activePlayer = player2
        gameStart(field1, player2)
    else:
        print(field1)
        if field1.winChecker() == True:
            print(activePlayer.name, "Победил!!!")
            break
        activePlayer = player1
        gameStart(field1, player1)
