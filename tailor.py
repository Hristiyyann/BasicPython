
tables = int(input("How many tables- "))
length = float(input("Length- "))
width = float(input("Width - "))

covers = kareta = tables
covers_area = (length+2*0.30) * (width+2*0.30)
kareta_area = (length/2) * (length/2)
kv_metri_covers = covers_area * tables
kv_metri_kareta = kareta_area * tables
price_covers = kv_metri_covers*7
price_kareta = kv_metri_kareta *9

all_price = price_covers + price_kareta

print(f"{all_price:.2f} USD")
bg_price  = all_price * 1.85
print(f"{bg_price:.2f} BGN ")
