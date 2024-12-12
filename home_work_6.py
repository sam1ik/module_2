# Задача "Все ли равны"

first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('Введите третье число: '))
if first == second == third:
    print('все 3 числа равны')
elif first == second or second == third or third == first:
    print('2 из 3 введенных чисел равны между собой')
else :
    print('количество равных чисел равны 0')