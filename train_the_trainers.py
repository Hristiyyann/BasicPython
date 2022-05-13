people = int(input())
needed_grades = 0
presentation = input()
total = total2 = presentation_count = 0
while presentation != 'Finish':
    presentation_count += 1
    total = needed_grades = 0
    while needed_grades < people:
        grade = float(input())
        total += grade
        needed_grades += 1
    total2 += total
    avr = total / people
    print(f'{presentation} - {avr:.2f}.')
    presentation = input()
new = total2 / (people * presentation_count)
print(f'Student\'s final assessment is {new:.2f}.')
