count_number = 1
end = int(input())
rows = 1
for i in range(1, end + 1):
    for j in range(1, rows + 1):
        print(f'{count_number} ', end='')
        count_number += 1
        if count_number > end:
            count_number = False
            break

    if not count_number:
        break
    print()
    rows += 1
