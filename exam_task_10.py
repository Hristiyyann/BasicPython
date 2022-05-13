space = float(input())
volume = input()
total = 0
flag = 0
total_suitcases = 0
while volume != 'End':
    volume = float(volume)
    total += volume
    if total_suitcases % 3 == 0:
        total += volume % 10
    if total > space:
        flag = 1
        break
    total_suitcases += 1

    volume = input()

if flag == 1:
    print(f'No more space!')
else:
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {total_suitcases} suitcases loaded.')