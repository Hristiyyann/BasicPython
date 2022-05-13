voucher = int(input())
item = input()
tickets = 0
orders = 0
while item != 'End':
    symbols = 0
    price = 0
    for char in item:
        symbols += 1

    if symbols > 8:
        price = ord(item[0]) + ord(item[1])
        flag = 2
    else:
        price = ord(item[0])
        flag = 1
    voucher -= price
    if voucher <= 0:
        break
    if flag == 1:
        orders += 1
    else:
        tickets += 1

    item = input()

print(tickets)
print(orders)
