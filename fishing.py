budget = int(input())
season = input()
fishers = int(input())
discount = 0
rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Winter':
    rent = 2600
else:
    rent = 4200

if fishers <= 6:
    discount = 0.1
elif 7 <= fishers <= 11:
    discount = 0.15
else:
    discount = 0.25

rent *= 1 - discount

if fishers % 2 == 0 and season != 'Autumn':
    rent *= 0.95

if rent > budget:
    print(f'Not enough money! You need {rent - budget:.2f} leva.')
else:
    print(f'Yes! You have {budget - rent:.2f} leva left.')
