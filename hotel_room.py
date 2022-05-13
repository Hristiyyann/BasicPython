month = input()
nights = int(input())
studio_discount = 0
apartment_discount = 0
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_discount = 0.05
    elif nights > 14:
        studio_discount = 0.3
        apartment_discount = 0.1
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_discount = 0.2
        apartment_discount = 0.1
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_discount = 0.1

apartment_price = apartment_price * nights
apartment_price = apartment_price * (1 - apartment_discount)

studio_price = studio_price * nights
studio_price = studio_price * (1 - studio_discount)

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
