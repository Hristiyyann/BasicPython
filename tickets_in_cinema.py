film_name = input()
count_of_seats = 0
kid_ticket = student_ticket = standard_ticket = total_tickets = 0
while film_name != 'Finish':
    free_seats = int(input())
    busy = count_of_seats = 0
    while count_of_seats < free_seats:
        kind_seat = input()
        if kind_seat == 'End':
            break
        count_of_seats += 1
        if kind_seat == 'kid':
            kid_ticket += 1
        elif kind_seat == 'student':
            student_ticket += 1
        elif kind_seat == 'standard':
            standard_ticket += 1

    busy = (count_of_seats/free_seats)*100
    print(f'{film_name} - {busy:.2f}% full.')
    film_name = input()
total_tickets = kid_ticket + student_ticket + standard_ticket
percent_student = (student_ticket/total_tickets) * 100
percent_kid = (kid_ticket/total_tickets)*100
percent_standard = (standard_ticket/total_tickets)*100


print(f'Total tickets: {total_tickets}')
print(f'{percent_student:.2f}% student tickets.')
print(f'{percent_standard:.2f}% standard tickets.')
print(f'{percent_kid:.2f}% kids tickets.')

