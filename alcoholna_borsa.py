whiskey_price = float(input("Price of the whiskey -"))
beer = float(input("Liters beer - "))
wine = float(input("Liters wine - "))
rakia = float(input("Liters rakia - "))
whiskey =float(input("Liters whiskey - "))

rakia_price = whiskey_price/2
print(rakia_price)
wine_price = rakia_price * 0.6
print(wine_price)
beer_price = rakia_price * 0.2
print(beer_price)

price = rakia_price * rakia + whiskey * whiskey_price + beer * beer_price + wine_price * wine
print(f"{price:.2f}")