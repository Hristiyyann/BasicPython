book_name = input()
book_for_search = input()
flag = 0
counter = 0
while book_for_search != 'No More Books':
    if book_for_search == book_name:
        flag = 1
        break
    book_for_search = input()
    counter += 1


if flag == 1:
    print(f'You checked {counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')
