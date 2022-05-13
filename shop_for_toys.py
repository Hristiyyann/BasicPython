puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

excursion = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

toys_count = puzzle + doll + bear + minion + truck
toys_price = puzzle * puzzle_price + doll * doll_price + bear * bear_price + minion * minion_price + truck * truck_price

if toys_count >= 50:
    toys_price *= 0.75

toys_price *= 0.9

if toys_price >= excursion:
    money = toys_price - excursion
    print(f"Yes! {money:.2f} lv left.")
else:
    money = excursion - toys_price
    print(f"Not enough money! {money:.2f} lv needed.")
