food = int(input()) * 1000
grams = input()
total = 0
flag = 0
while grams != 'Adopted':
    grams = int(grams)
    total += grams

    if total > food:
        flag = 1

    grams = input()

if flag != 1:
    print(f'Food is enough! Leftovers: {food - total} grams.')
else:
    print(f'Food is not enough. You need {total - food} grams more.')
