film_name = input()
kid_ticket = 0
standard_ticket = 0
student_ticket = 0
total = 0
tickets_film = 0
while film_name != 'Finish':
    chairs = int(input())
    tickets_film = 0
    for char in range(0, chairs):
        kind_ticket = input()
        if kind_ticket == 'End':
            break
        total += 1
        tickets_film += 1

        if kind_ticket == 'kid':
            kid_ticket += 1
        elif kind_ticket == 'standard':
            standard_ticket += 1
        elif kind_ticket == 'student':
            student_ticket += 1
    print(f'{film_name} - {(tickets_film / chairs) * 100:.2f}% full.')
    film_name = input()
print(f'Total tickets: {total}')
print(f'{(student_ticket / total) * 100:.2f}% student tickets.')
print(f'{(standard_ticket / total) * 100:.2f}% standard tickets.')
print(f'{(kid_ticket / total) * 100:.2f}% kids tickets.')

