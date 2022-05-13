days = int(input())
kind_room = input()
grade = input()

days = days - 1
discount = 0
price = 0
end_price = 0

if kind_room == 'apartment':
    price = 25
    if days <= 10:
        discount = 0.3
    elif 10 < days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.5
elif kind_room == 'president apartment':
    price = 35
    if days <= 10:
        discount = 0.1
    elif 10 < days <= 15:
        discount = 0.15
    else:
        discount = 0.2
elif kind_room == 'room for one person':
    price = 18

price = price * days
price = price * (1 - discount)

if grade == 'positive':
    plus = 0.25
    price += price * plus
elif grade == 'negative':
    minus = 0.1
    price -= price * minus

print(f'{price:.2f}')
