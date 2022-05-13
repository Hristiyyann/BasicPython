ceil_border_first = int(input())
ceil_border_second = int(input())
ceil_border_third = int(input())

for first in range(1, ceil_border_first + 1):
    for second in range(1, ceil_border_second + 1):
        for third in range(1, ceil_border_third + 1):
            if first % 2 == 0 and third % 2 == 0:
                if second == 2 or second == 3 or second == 5 or second == 7:
                    print(f'{first} {second} {third}')
