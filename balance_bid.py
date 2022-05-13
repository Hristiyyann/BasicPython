money_for_deposit = input()
total = 0

while money_for_deposit != 'NoMoreMoney':
    money_for_deposit = float(money_for_deposit)
    if money_for_deposit < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {money_for_deposit:.2f}')
    total += money_for_deposit
    money_for_deposit = input()

print(f'Total: {total:.2f}')
