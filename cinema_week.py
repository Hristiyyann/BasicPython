film = input()
hall = input()
tickets = int(input())
price = 0
if film == 'A Star Is Born':
    if hall == 'normal':
        price = 7.50
    elif hall == 'luxury':
        price = 10.50
    else:
        price = 13.50
elif film == 'Bohemian Rhapsody':
    if hall == 'normal':
        price = 7.35
    elif hall == 'luxury':
        price = 9.45
    else:
        price = 12.75
elif film == 'Green Book':
    if hall == 'normal':
        price = 8.15
    elif hall == 'luxury':
        price = 10.25
    else:
        price = 13.25
elif film == 'The Favourite':
    if hall == 'normal':
        price = 8.75
    elif hall == 'luxury':
        price = 11.55
    else:
        price = 13.95

print(f'{film} -> {price*tickets:.2f} lv.')