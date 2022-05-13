beginning = int(input())
end = int(input())
magic_num = int(input())
flag = 0
operation_count = 0
for i in range(beginning, end + 1):
    for j in range(beginning, end + 1):
        operation_count += 1
        if i + j == magic_num:
            flag = 1
            print(f'Combination N:{operation_count} ({i} + {j} = {magic_num})')
            break
    if flag:
        break

if flag == 0:
    print(f'{operation_count} combinations - neither equals {magic_num}')
