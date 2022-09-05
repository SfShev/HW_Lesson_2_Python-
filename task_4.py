# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint


num = int(input("Введите число: "))

def list_elements (x):
    list_elem = []
    for i in range(- num,num + 1):
        list_elem.append (randint (- num, num +1))
    return list_elem

x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))

def multiplication(list_elem):
    for i in range(len(list_elem)):
        mult = list_elem[x -1]*list_elem[y - 1]
    print(f'Произведение чисел на позициях {x} и {y} в списке {list_elem} \n{list_elem[x-1]} * {list_elem[y-1]} =', mult)


multiplication(list_elements(num))