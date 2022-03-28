# Напишите функцию, которая возводит в степень число, которое передается
# в параметрах, если степень не отрицательная. Первый параметр - число,
# второй - степень, в которую его нужно возвести.


def chislo_v_stepen (a,b):
    return a**b if b>0 else print()

step=chislo_v_stepen(2,3)
print(step)
step1=chislo_v_stepen(2,-4)
print(step1)
