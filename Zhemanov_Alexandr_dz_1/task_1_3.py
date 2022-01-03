#!/usr/bin/env python3

"""conjugation word процент from 1 to 100"""

phrase_without_end: str = "процент"

for i in range(1, 100 + 1):
    # exceptions + 5 - 9 end
    if (i % 10 == 0 or
            11 <= i >= 14 or
            5 <= i % 10 <= 9):
        print(i, phrase_without_end + "ов")
    elif 2 <= i % 10 < 5:
        print(i, phrase_without_end + "a")
    elif i % 10 == 1:
        print(i, phrase_without_end)
