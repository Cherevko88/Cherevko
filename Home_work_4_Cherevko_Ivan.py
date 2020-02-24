"""Задание № 1
    Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]).
Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81. """

numbers = [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]
a = []
for number in numbers:
    if 18 < number < 81:
        a.append(number)
print(a)
''' Второй вариант решения '''
a = [number for number in numbers if 18 < number < 81]
print(a)

'''Задание № 2 
    Дан словарь продавцов и цен на какой то телефон у разных продавцов на hotline: 
{ ‘citrus’: 47.999,‘istudio’: 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245,‘buy.ua’: 38.324,‘g-store’: 37.166,
‘ipartner’: 38.988,‘sota’: 37.720 }.
    Написать программу, которая выдаст список имен продавцов, чьи цены попадают в определенный диапазон. 
Диапазон задается как два числовых аргумента.'''

hotline = {'citrus': 47.999,'istudio': 42.999,'moyo': 49.999,'royal-service': 37.245,'buy.ua': 38.324,
'g-store': 37.166,'ipartner': 38.988,'sota': 37.720}
arg1 = 38
arg2 = 47
a = []
prices = list(hotline.values())
print(list(hotline.values()))
for price in prices:
    if arg1 < price < arg2:
        a.append(price)
list_1 = []
for i in hotline.items():
    if i[1] in a:
        list_1.append(i[0])
print(list_1)

"""
Задание № 3*
Есть строка произвольной длины. Написать программу, которая должна создать словарь следующего содержания:
ключ - количество букв в слове,
значение - список слов с таким количеством букв.
Отдельным ключом ("0") количество пробелов и знаки препинания ("punctuation"). Например:
{
"0": количество пробелов в строке,
"1": list слов из одной буквы,
"2": list слов из двух букв,
"3": list слов из трех букв и т.д.
"punctuation": tuple уникальных знаков препинания}"""


sentence = "а@, б#, в$, аа! бб$ вв ааа ббб аааа бббб ввввв ггггг шестьь шестьь семьььь семьььь восемььь восемььь ,"
sentence = sentence.lower()
space = sentence.count(" ")
punctuation = (")!@#$%^&*()_+=-<>?,./")
vocabulary = {}
s =[]
for simvol in sentence:
    s1 = " "
    if simvol in punctuation:
        simvol.count(punctuation)
        s1 = simvol
        s.append(s1)
simvols = tuple(s)

def func(a):
    return (a not in punctuation)
sentence1 = ''.join(list(filter(func, sentence)))
sentence_split = sentence1.split()

w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
w6 = []
w7 = []
w8 = []
w9 = []
w10 = []

vocabulary["0"] = space
for word in sentence_split:
    word1 = []
    if len(word) == 1:
        word1 = word
        w1.append(word1)
        vocabulary["1"] = w1
    if len(word) == 2:
        word1 = word
        w2.append(word1)
        vocabulary["2"] = w2
    if len(word) == 3:
        word1 = word
        w3.append(word1)
        vocabulary["3"] = w3
    if len(word) == 4:
        word1 = word
        w4.append(word1)
        vocabulary["4"] = w4
    if len(word) == 5:
        word1 = word
        w5.append(word1)
        vocabulary["5"] = w5
    if len(word) == 6:
        word1 = word
        w6.append(word1)
        vocabulary["6"] = w6
    if len(word) == 7:
        word1 = word
        w7.append(word1)
        vocabulary["7"] = w7
    if len(word) == 8:
        word1 = word
        w8.append(word1)
        vocabulary["8"] = w8
    if len(word) == 9:
        word1 = word
        w9.append(word1)
        vocabulary["9"] = w9
    if len(word) == 10:
        word1 = word
        w10.append(word1)
        vocabulary["10"] = w10
vocabulary["punctuation"] = simvols
for key, value in vocabulary.items():
    print("{0}: {1}".format(key,value))




