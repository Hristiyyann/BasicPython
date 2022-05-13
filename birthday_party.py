rent = float(input())

total = rent
cake = rent * 0.2
drinks = cake - (0.45 * cake)
animator = (1 / 3) * rent

total += cake + drinks + animator

print(total)
