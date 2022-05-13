hour = int(input())
minutes = int(input())

if minutes + 15 >= 60:
    hour += 1

    if minutes <= 44:
        minutes += 15
    else:
        minutes = abs(45 - minutes)

    if hour + 1 > 23:
        hour = 0
else:
    minutes += 15

if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
