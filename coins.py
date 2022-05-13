width = int(input())
length = int(input())

pieces = width * length
taken_pieces = 0

while taken_pieces < pieces:
    count_pieces_for_taking = input()
    if count_pieces_for_taking == 'STOP':
        break
    count_pieces_for_taking = int(count_pieces_for_taking)
    taken_pieces += count_pieces_for_taking
if taken_pieces > pieces:
    print(f'No more cake left! You need {taken_pieces - pieces} pieces more.')
else:
    print(f'{pieces - taken_pieces} pieces are left.')
