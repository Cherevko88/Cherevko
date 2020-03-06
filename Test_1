import random

def diapas():
    """Функция просит ввести игрока диапазон макс. числа """
    diapason = input("Ведите максимально возможное число\n")
    try:
        diapason = int(diapason)
        return diapason
    except ValueError:
        return diapas()

def num():
    """Функция просит ввести игрока максимальное число"""
    number = input("На какое число сделаете выбор?\n")
    try:
        number = int(number)
        return number
    except ValueError:
        return num()


print("Добрый день игрок")
def tron():
    the_end = ("Хорошего дня!")
    ran = random.randint(1,(diapas()))

    while True:
        if ran != num():
            print("Правильный ответ -->", ran)
            return tron()
        if ran == num():
            povtor = input("Если хотите повторить игру нажмите \"Y\", если нет, нажмите \"N\"\n")
            for i in povtor:
                if i == str.lower("Y"):
                    return tron()
                if i == str.lower("N"):
                    return the_end
                else:
                    print("Вы ввели не Y и не N")
print(tron())
