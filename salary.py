tabs = int(input())
salary = int(input())
flag = 0
for count in range(tabs):
    name_tab = input()

    if name_tab == 'Facebook':
        salary -= 150
    elif name_tab == 'Instagram':
        salary -= 100
    elif name_tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        flag = 1
        break

if flag == 1:
    print('You have lost your salary.')
else:
    print(f'{salary}')
