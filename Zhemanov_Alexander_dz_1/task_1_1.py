#!/usr/bin/env python3

"""convert x sec to d day h hour m minute and s sec"""
# CONST
SEC_IN_MINUTE = 60
SEC_IN_HOUR = SEC_IN_MINUTE * 60
SEC_IN_DAY = SEC_IN_HOUR * 24

in_sec_str = input("количество секунд: ")
output_msg:str = ""

try:

    sec = int(in_sec_str)

    if sec >= SEC_IN_DAY:
        output_msg += str(sec // SEC_IN_DAY) + " дн "
        sec %= SEC_IN_DAY

    if sec >= SEC_IN_HOUR:
        output_msg += str(sec // SEC_IN_HOUR) + " час "
        sec %= SEC_IN_HOUR

    if sec >= SEC_IN_MINUTE:
        output_msg += str(sec // SEC_IN_MINUTE) + " мин "
        sec %= SEC_IN_MINUTE

    output_msg += str(sec) + " сек"
    print(output_msg)

except ValueError:
    print(in_sec_str, "isn't number.")
