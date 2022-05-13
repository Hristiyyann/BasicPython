minutes = int(input())
walks = int(input())
calories = int(input())

minutes *= walks
new_calories = minutes * 5

if new_calories > calories // 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {new_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {new_calories}.")
