film = input()
redove = int(input())
coloni = int(input())
price = 0
sits = redove * coloni

if film == 'Premiere':
    price = 12
elif film == 'Normal':
    price = 7.50
elif film == 'Discount':
    price = 5

print(f'{(price*sits):.2f} leva')
