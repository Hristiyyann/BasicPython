count_bad_grades = int(input())
last_question = ''
total = 0
count = 0
bad_grades = 0
flag = 0
while 1:
    question = input()
    if question == 'Enough':
        flag = 1
        break
    else:
        mark = int(input())
        if mark <= 4:
            bad_grades += 1
            if bad_grades == count_bad_grades:
                print(f'You need a break, {bad_grades} poor grades.')
                break
        total += mark
        last_question = question
        count += 1
if flag:
    print(f'Average score: {total / count:.2f}')
    print(f'Number of problems: {count}')
    print(f'Last problem: {last_question}')