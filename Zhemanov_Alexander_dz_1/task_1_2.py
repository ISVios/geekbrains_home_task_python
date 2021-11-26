#!/usr/bin/env python3

"""output:
    sum of odd elem(xyz..) sum(x+y+z) which % 7
    sum of odd (elem + 17) which % 7
"""

def sum_of_num(num:int):
    res = 0

    while num > 0:
        res += num % 10
        num //= 10
    return res

# lazy list
list_of_odd = range(1, 1000 + 1, 2)

sum_with_17:int = 0
sum_without_17:int = 0

for elem in list_of_odd:

    cube = elem ** 3
    cube_with_17 = (elem + 17) ** 3

    if sum_of_num(cube) % 7 == 0:
        sum_without_17 += cube

    if sum_of_num(cube_with_17) % 7 == 0:
        sum_with_17 += cube_with_17

print("сумма без 17:", sum_without_17)
print("сумма c 17:", sum_with_17)

