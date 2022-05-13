films = int(input())
film_name = input()
rating = float(input())
max_rate = rating
max_rate_film = film_name
min_rate = rating
min_rate_film = film_name
average = rating

for film in range(1, films):
    film_name = input()
    rating = float(input())

    if rating > max_rate:
        max_rate = rating
        max_rate_film = film_name
    if rating < min_rate:
        min_rate = rating
        min_rate_film = film_name

    average += rating

print(f'{max_rate_film} is with highest rating: {max_rate:.1f}')
print(f'{min_rate_film} is with lowest rating: {min_rate:.1f}')
print(f'Average rating: {average / films:.1f}')
