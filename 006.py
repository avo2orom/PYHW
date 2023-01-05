# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

text = input('Введите число: ')
text = text.replace('.', '').replace(',', '')
number = int(text)
sum = 0
result = 0
for i in range(number):
    sum = number - (number % 10)
    result = result + (number -sum)
    number = number//10
print(result)