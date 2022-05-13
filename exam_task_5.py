fruit = input()
shape = input()
sets = int(input())
price = 0
if shape == 'big':
    if fruit == 'Watermelon':
        price = 28.70
    elif fruit == 'Mango':
        price = 19.60
    elif fruit == 'Pineapple':
        price = 24.80
    else:
        price = 15.20

    price *= 5
else:
    if fruit == 'Watermelon':
        price = 56
    elif fruit == 'Mango':
        price = 36.66
    elif fruit == 'Pineapple':
        price = 42.10
    else:
        price = 20

    price *= 2

price *= sets

if 400 < price < 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f'{price:.2f} lv.')
