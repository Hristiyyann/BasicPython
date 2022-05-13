name = input()
grades_count = 1
total = avr = 0
bad_grade = 0
flag = 0

while grades_count <= 12:
    grade = float(input())
    if grade < 4:
        bad_grade += 1
        if bad_grade == 2:
            flag = 1
            print(f'{name} has been excluded at {grades_count} grade')
            break
    else:
        total += grade
        grades_count += 1
if flag == 0:
    avr = total / 12
    print(f'{name} graduated. Average grade: {avr:.2f}')
