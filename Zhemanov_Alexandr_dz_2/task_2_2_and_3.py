#!/usr/bin/env python3

""" task 2 """

# We can solve with pop and push(append).

input_list = ['в', '5', 'часов', '17', 'минут',
              'температура', 'воздуха', 'была', '+5', 'градусов']
length_of_list: int = len(input_list)
store_id = id(input_list)

print(f"id before {store_id}")

for _ in range(length_of_list):  # pyright change i to _

    elem = input_list.pop(0)

    # no nessary use isalnum in here but I use
    if  elem.isdigit() and elem.isalnum():
        input_list.append(f'"{int(elem):02d}"')
        # or   ['"', "00", '"']
        # input_list.append('"')
        # input_list.append(f'{int(elem):02d}')
        # input_list.append('"')

    elif elem[0] == "+" and elem[1].isdigit():
        input_list.append(f'"+{int(elem):02d}"')
        # or   ['"', "+00", '"']
        # input_list.append('"')
        # input_list.append(f'+{int(elem):02d}')
        # input_list.append('"')

    else:
        input_list.append(elem)

print(' '.join(input_list))

print(f"id after {id(input_list)}")
