days = int(input())
food = float(input())
counter = 1
sum_food = 0
sum_food_dog = 0
sum_food_cat = 0
biscuits = 0

for counter in range(1, days + 1):
    quantity_dog = int(input())
    quantity_cat = int(input())
    sum_food_cat += quantity_cat
    sum_food_dog += quantity_dog
    sum_food += quantity_dog + quantity_cat

    if counter % 3 == 0:
        biscuits += (quantity_cat + quantity_dog) * 0.1

print(f'Total eaten biscuits: {biscuits:.0f}gr.')
print(f'{(sum_food / food) * 100:.2f}% of the food has been eaten.')
print(f'{(sum_food_dog / sum_food) * 100:.2f}% eaten from the dog.')
print(f'{(sum_food_cat / sum_food) * 100:.2f}% eaten from the cat.')
