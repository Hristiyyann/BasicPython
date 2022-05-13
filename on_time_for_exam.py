hour_for_exam = int(input())
minutes_for_exam = int(input())
hour_for_arriving = int(input())
minutes_for_arriving = int(input())

exam_minutes = (hour_for_exam * 60) + minutes_for_exam
arrive_minutes = (hour_for_arriving * 60) + minutes_for_arriving

if exam_minutes == arrive_minutes:
    print('On time')
elif exam_minutes > arrive_minutes:
    if exam_minutes - arrive_minutes <= 30:
        print('On time')
        print(f'{exam_minutes - arrive_minutes} minutes before the start')
    elif exam_minutes - arrive_minutes < 60:
        print('Early')
        print(f'{exam_minutes - arrive_minutes} minutes before the start')
    else:
        print('Early')
        if (exam_minutes - arrive_minutes) % 60 < 10:
            print(f'{(exam_minutes - arrive_minutes) // 60}:0{(exam_minutes - arrive_minutes) % 60} hours before the start')
        else:
            print(f'{(exam_minutes - arrive_minutes) // 60}:{(exam_minutes - arrive_minutes) % 60} hours before the start')
else:
    if arrive_minutes - exam_minutes < 60:
        print('Late')
        print(f'{arrive_minutes-exam_minutes} minutes after the start')
    else:
        print('Late')
        if (arrive_minutes - exam_minutes) % 60 < 10:
            print(
                f'{(arrive_minutes - exam_minutes) // 60}:0{(arrive_minutes - exam_minutes) % 60} hours after the start')
        else:
            print(
                f'{(arrive_minutes - exam_minutes) // 60}:{(arrive_minutes - exam_minutes) % 60} hours after the start')
