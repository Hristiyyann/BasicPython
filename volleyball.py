import math

year = input()
holidays = int(input())
weekends = int(input())

total = (48 - weekends) * (3 / 4)
total += weekends
total += holidays * (2 / 3)

if year == 'leap':
    total *= 1.15

total = math.floor(total)
print(total)
