width = float(input())
length = float(input())
height = float(input())
area = width * length * height
total = 0
flag = 0

while 1:
    command = input()
    if command == 'Done':
        break

    command = int(command)
    total += command
    if total > area:
        flag = 1
        break

if flag == 0:
    print(f"{area - total:.0f} Cubic meters left.")
else:
    print(f'No more free space! You need {total - area:.0f} Cubic meters more.')
