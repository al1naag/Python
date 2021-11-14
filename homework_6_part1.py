import random

# Python Functions, Lists
#  - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.

# 1. Написать скрипт который в создаст список целых чисел.

list1 = []
for x in range(1, 70):
    list1.append(x)
print(list1)

# 2. Написать скрипт который в создаст список целых чётных чисел.

list2 = []
for x in range(0, 70, 2):
    list2.append(x)
print(list2)

# 3. Написать скрипт который в создаст список целых нечётных чисел.

list3 = []
for x in range(1, 70, 2):
    list3.append(x)
print(list3)

# 4. Написать скрипт который из списка целых чисел выведет чётные числа.

for x in list1:
    if x % 2 == 0:
        print(x)

# 5. Написать скрипт который из списка целых чисел выведет нечётные числа.

for x in list1:
    if x % 2 != 0:
        print(x)

# 6. Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.

for x in list1:
    if x % 5 == 0:
        print(x)

# 7. Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
count = 0
for x in list1:
    if x % 5 == 0:
        count = count + 1
print(count)

# 8. Написать скрипт который в создаст список целых рандомных чисел.
randomlist = []
for i in range(0, 10):
    i = random.randint(1, 10)
    randomlist.append(i)
print(randomlist)


# 9. Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.

def splits(lst, x):
    for i in range(0, len(lst), x):
        yield list1[i:i + x]


print(list((splits)(list1, 10)))


# 10. Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.

evenlist = []
oddlist = []
for x in list1:
    if x % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)
print(evenlist)
print(oddlist)

# 11. Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.

stars_5 = []
stars_5.append([6,7,8,9,10])
stars_5.append([1,2,3,4,5])
print(stars_5)

# 12. Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars

stars_5 = []
stars_5.append([6,7,8,9,10])
stars_5.append([1,2,3,4,5])
print(sum(stars_5[0]))
print(sum(stars_5[1]))
# 13. Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка.
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100.
# Если какого-то списка не получится, то вместо него вернуть текст “No lists”

def stars_5():
    stars_5 = []
    stars_5.append([6, 7, 8, 9, 10])
    stars_5.append([1, 2, 3, 4, 5])
    print(sum(stars_5[0]))
    print(sum(stars_5[1]))
    if sum(stars_5[0]) >= 100:
        print('sum >= 100', stars_5[0])
        if sum(stars_5[1]) >= 100:
            print('sum >= 100', stars_5[1])
    elif sum(stars_5[0]) < 100:
        print('sum < 100',stars_5[0])
        if sum(stars_5[1]) < 100:
            print('sum < 100',stars_5[1])
    else:
        print('No lists')
    return
stars_5()
