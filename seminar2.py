#  Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

 

n = input('Введите число: \n')
 
suma = 0
 
for digit in n:
    if digit.isdigit():
        suma += int(digit)
        
print("Сумма цифр числа =", suma)