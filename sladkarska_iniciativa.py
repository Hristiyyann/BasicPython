days = int(input())
cookers = int(input())
cakes = int(input())
gofra = int(input())
pancakes = int(input())

cakes_price = 45
gofra_price = 5.80
pancakes_price = 3.20
price = (cakes*cakes_price + gofra*gofra_price + pancakes*pancakes_price)*cookers
price_for_all_days = days * price
konsumativi = price_for_all_days * 0.125
price_for_all_days = price_for_all_days - konsumativi

print(price_for_all_days)