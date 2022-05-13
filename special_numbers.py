N = int(input())
flag = 0
for number in range(1111, 10000):
    number = str(number)
    flag = 0
    if number[1] == '0' or number[2] == '0' or number[3] == '0':
        pass
    else:
        for digit in number:
            digit = int(digit)
            if N % digit != 0:
                flag = 1
        if not flag:
            print(number, end=' ')
