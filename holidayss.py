needed_money_for_trip = float(input())
available_money_for_trip = float(input())
spending_days_in_a_row = 0
counter_for_days = 0
flag = 0

while available_money_for_trip < needed_money_for_trip and spending_days_in_a_row < 5:
    command = input()
    money = float(input())
    counter_for_days += 1

    if command == 'save':
        spending_days_in_a_row = 0
        available_money_for_trip += money
    else:
        spending_days_in_a_row += 1
        available_money_for_trip -= money
        if available_money_for_trip < 0:
            available_money_for_trip = 0

if spending_days_in_a_row == 5:
    print('You can\'t save the money.')
    print(counter_for_days)
if available_money_for_trip >= needed_money_for_trip:
    print(f'You saved the money for {counter_for_days} days.')
