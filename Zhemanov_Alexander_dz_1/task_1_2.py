#!/usr/bin/env python3

"""output:
    sum of odd elem which % 7
    sum of odd (elem + 17) which % 7
"""

# lazy list
list_of_odd = range(1, 1000 + 1, 2)

sum_with_17:int = 0
sum_without_17:int = 0

for elem in list_of_odd:

    cube = elem ** 3
    cube_with_17 = (elem + 17) ** 3

    if cube % 7 == 0:
        sum_without_17 += cube

    if cube_with_17 % 7 == 0:
        sum_with_17 += cube_with_17

print("сумма без 17:", sum_without_17)
print("сумма c 17:", sum_with_17)

