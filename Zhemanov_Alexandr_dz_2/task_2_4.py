#!/usr/bin/env python3

""" task 4 """

input_list = ['инженер-конструктор Игорь',
            'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
answer = {}

for string in input_list:
    correct_name = string.split()[-1].capitalize()
    print(f"Привет, {correct_name}!")
