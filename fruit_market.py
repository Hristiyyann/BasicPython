price_strawberry = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberry = float(input())
kg_strawberry = float(input())

price_raspberry = price_strawberry / 2
price_oranges = price_raspberry - (price_raspberry * 0.4)
price_bananas = price_raspberry - (price_raspberry * 0.8)

price = price_bananas * kg_bananas + price_oranges * kg_oranges + price_raspberry * kg_raspberry + price_strawberry * kg_strawberry

print(price)
