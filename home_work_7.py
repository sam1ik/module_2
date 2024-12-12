my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6,5]
print('Исходные данные:', my_list)
indx = 0
while indx < len(my_list):
    number = my_list[indx]
    indx = indx + 1
    if number == 0:
        continue
    elif number < 0:
        break
    print(number)