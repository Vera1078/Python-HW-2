#  Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

 
print('Задача на поиск суммы цифр числа')
n = input('Введите число: \n')
 
suma = 0
 
for digit in n:
    if digit.isdigit():
        suma += int(digit)
        
print("Сумма цифр числа =", suma)
print()
print()

#  Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Задача на вывод произведений чисел от 1 до n')
def factorial (number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

n = int(input('Введите целое положительное число: '))
if n <= 0:
    print('Число введено неверно')

for i in range(1, n + 1):
    
    if i == n: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')

print()
print()

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

print('Задача на вывод списка из n чисел последовательности (1+1/n)^n и их суммы')
n = int(input("Введите целое положительное число: "))
numbers = {n : round(pow((1 + 1 / n), n), 2) for n in range(1, n + 1)}

val_sum = 0
for j in numbers.values():
    val_sum += j

print(f'Для n = {n} {numbers}')
print(f'Сумма значений = {round(val_sum, 2)}')

print()
print()


#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

print('Задача на вывод произведений элементов от -N до N списка размером N')
from random import randint
N = int(input('Введите число N: '))
numbers = []
for i in range(1, N +1 ):
    numbers.append(randint (-N, N))
print(numbers)

x = int(input('Введите номер позиции для первого элемента: '))
while x > len(numbers):
    print('Значение введено неверно. Данный номер позиции отсутствует.') 
    x = int(input('Введите номер позиции для первого элемента: '))
      
y = int(input('Введите номер позиции для второго элемента: '))
while y > len(numbers):
    print('Значение введено неверно. Данный номер позиции отсутствует.') 
    y = int(input('Введите номер позиции для второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Произведение элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)
print()
print()

# Реализуйте алгоритм перемешивания списка.

print('Задача на перемешивание списка')
import random
def mix_list(list_original):
   
    list = list_original[:]
   
    list_length = len(list)
    for i in range(list_length):
        
        index_aleatory = random.randint(0, list_length - 1)
     
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
 
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)