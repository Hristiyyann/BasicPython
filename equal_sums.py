beginng = int(input())
end = int(input())
sum_1 = sum_2 = sum = 0
for number in range(beginng, end + 1):
    number = str(number)
    index = 0
    for digit in number:
        if index % 2 == 0:
            digit = int(digit)
            sum_2 += digit
        else:
            digit = int(digit)
            sum_1 += digit
        index += 1
    if sum_1 == sum_2:
        print(number)
