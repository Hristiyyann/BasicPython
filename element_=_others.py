numbers = int(input("Numbers = "))
max_num = 0
sum_num = 0
for count in range(numbers):
    num = int(input())
    if num > max_num:
        max_num = num

    sum_num += num
if sum_num== max_num:
    print(f"Yes! {sum}")
else:
    razlika = abs(sum_num - max_num)
    print(f"No! {razlika}")
