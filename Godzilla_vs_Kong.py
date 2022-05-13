budget = float(input())
actors = int(input())
price_clothes_actor = float(input())

decor = budget * 0.1

price_clothes_actor *= actors

if actors > 150:
    price_clothes_actor *= 0.9

required_budget = decor + price_clothes_actor

if required_budget > budget:
    more_money = required_budget - budget
    print("Not enough money!")
    print(f"Wingard needs {more_money:.2f} leva more.")
else:
    left_money = budget - required_budget
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
