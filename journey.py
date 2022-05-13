budget = float(input())
season = input()
place = ''
point = ''
price = 0

if budget <= 100:
    place = 'Somewhere in Bulgaria'
    if season == 'summer':
        point = 'Camp'
        price = 0.3
    elif season == 'winter':
        point = 'Hotel'
        price = 0.7
elif budget <= 1000:
    place = 'Somewhere in Balkans'
    if season == 'summer':
        point = 'Camp'
        price = 0.4
    elif season == 'winter':
        point = 'Hotel'
        price = 0.8
elif budget > 1000:
    place = 'Somewhere in Europe'
    point = 'Hotel'
    price = 0.9

price = budget * price

print(f'{place}')
print(f'{point} - {price:.2f}')
