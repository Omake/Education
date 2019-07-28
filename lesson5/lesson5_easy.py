# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def massFolderCreator():
    i = 1
    while i < 10:
        dirPath = os.path.join(os.getcwd(), f"dir_{i}")
        os.mkdir(dirPath)
        i += 1


def deleteMassFolders():
    i = 1
    while i < 10:
        dirPath = os.path.join(os.getcwd(), f"dir_{i}")
        shutil.rmtree(dirPath)
        i += 1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def printFolders():
    folderElemens = os.listdir(os.getcwd())
    for elem in folderElemens:
        if os.path.isdir(elem) is True:
            print(elem)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copyCurrentFile():
    thisFile = os.path.join(os.getcwd(), __file__)
    copiedFile = os.path.join(os.getcwd(), f"{__file__}_copy.py")
    shutil.copyfile(thisFile, copiedFile)


# В задании normal было сказано использовать функции из задания easy, но я не совсем понял смысл, т.к. в нормале просят
# Выполнять то, что не делалось в easy. Так что я просто дописал новые функции ниже

def changeCurrentFolder(userPath):
    try:
        os.chdir(userPath)
        print(f"Успешно перешли в папку  {userPath}")
    except Exception:
        print(f"Не удалось перейти в папку  {userPath}")


def printAllElements():
    print(os.listdir(os.getcwd()))


def deleteUsersFolder(userPath):
    try:
        shutil.rmtree(userPath)
        print(f"Папка {userPath} успешно удалена!")
    except Exception:
        print(f"Не удалось удалить папку {userPath}")

def createUsersFolder(userPath):
    try:
        os.mkdir(userPath)
        print(f"Папка {userPath} успешно создана!")
    except Exception:
        print(f"Не удалось создать папку {userPath}")