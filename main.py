# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import random
#
# coins = int(input("Enter the quantity of coins: "))
# coin_array = [0]*coins
# index = 0
# zeros_quan = 0
# ones_quan = 0
# while index < len(coin_array):
#     coin_array[index] = random.randint(0, 1)
#     if coin_array[index] == 0:
#         zeros_quan += 1
#     else:
#         ones_quan += 1
#     index += 1
# print(coin_array)
# if zeros_quan > ones_quan:
#     print(coins-zeros_quan)
# else:
#     print(coins-ones_quan)





# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# # Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# # Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# import math
# summa = int(input("Enter the summa of 2 integers: "))
# s = summa
# if s<0:
#     print("The number must be positive integer!")
#
# product = int(input("Enter the product of 2 integers: "))
# p = product
# if p<0:
#     print("The number must be positive integer!")
#
# D = math.pow(s,2) - 4*p
# if D == 0:
#     y1 = s/2
#     x1 = p/y
#     if y1 <= 1000 and x1 <= 1000:
#       print(f"X is {x1}, Y is {y1}")
#     else:
#       print("The pair(-s) are bigger than 1000")
# elif D < 0:
#     print("The solution has no natural numbers")
# else:
#     y1 = (s + math.sqrt(D))/2
#     y2 = (s-math.sqrt(D))/2
#     x1 = p / y1
#     x2 = p / y2
#     if y1 <= 1000 and x1 <= 1000:
#       print(f"The first pair of X,Y is {x1,y1}\nThe second pair is {x2,y2}")
#     else:
#       print("The pair(-s) are bigger than 1000")





# # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# number = int(input("Enter a positive integer number: "))
# comparative_number = 2
# integer_power = 1
# while comparative_number <= number:
#     comparative_number *= 2
#     integer_power += 1
# if comparative_number == number:
#     print(integer_power)
# else:
#     print(integer_power-1)