change = int(float(input()) * 100)
money_for_changing = 0

while change > 0:
    money_for_changing += 1
    if change >= 200:
        change -= 200
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 20:
        change -= 20
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 2:
        change -= 2
    else:
        change -= 1

print(money_for_changing)