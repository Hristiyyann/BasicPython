flowers = input()
number_flowers = int(input())
budget = int(input())
discount = 0
price = 0
flag = 0

if flowers == 'Roses':
    price = 5
    if number_flowers > 80:
        discount = 0.1
elif flowers == 'Dahlias':
    price = 3.80
    if number_flowers > 90:
        discount = 0.15
elif flowers == 'Tulips':
    price = 2.80
    if number_flowers > 80:
        discount = 0.15
elif flowers == 'Narcissus':
    price = 3
    flag = 1
    if number_flowers < 120:
        price += price * 0.15
elif flowers == 'Gladiolus':
    price = 2.5
    flag = 1
    if number_flowers < 80:
        price += price * 0.2

if flag == 0:
    price = price * (1 - discount)
    price = price * number_flowers
else:
    price = price * number_flowers
if price > budget:
    need_money = price - budget
    print(f'Not enough money, you need {need_money:.2f} leva more.')
else:
    more_money = budget - price
    print(f'Hey, you have a great garden with {number_flowers} {flowers} and {more_money:.2f} leva left.')
