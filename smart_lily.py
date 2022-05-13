age = int(input())
washing_machine = float(input())
price_for_toy = int(input())
saved_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        saved_money += (birthday * 10 / 2) - 1
    else:
        saved_money += price_for_toy
difference = abs(saved_money - washing_machine)

if saved_money >= washing_machine:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
