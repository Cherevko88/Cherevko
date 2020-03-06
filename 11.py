
import random
print("Добрый день игрок")


def tron():

    the_end = ("Хорошего дня!")
    while True:
        diapason = input("Ведите максимально возможное число\n")
        try:
            diapason = int(diapason)
        except ValueError:
            print("Вы ввели не число!")
            return tron()
        ran = random.randint(1, diapason)
        number = input("На какое число сделаете выбор?\n")
        try:
            number = int(number)
        except ValueError:
            print("Вы ввели не число!")
            return tron()
        print("Правильный ответ -->", ran)
        if ran != number:
            continue
        if ran == number:
            povtor = input("Если хотите повторить игру нажмите \"Y\", если нет, нажмите \"N\"\n")
            for i in povtor:
                if i == str.lower("Y"):
                    return tron()
                if i == str.lower("N"):
                    return the_end
                else:
                    print("Вы ввели не Y и не N")

print(tron())

