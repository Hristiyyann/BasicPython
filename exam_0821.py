clients = int(input())
price_for_clients = 0

for client in range(clients):
    total = 0
    purchased_products = 0
    product = input()

    while product != 'Finish':
        purchased_products += 1
        if product == 'basket':
            total += 1.5
        elif product == 'wreath':
            total += 3.8
        else:
            total += 7
        product = input()

    if purchased_products % 2 == 0:
        total *= 0.8
    price_for_clients += total

    print(f'You purchased {purchased_products} items for {total:.2f} leva.')

print(f'Average bill per client is: {price_for_clients /clients:.2f} leva.')
