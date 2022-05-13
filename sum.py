number = int(input("Number"))
sum_even=0
sum_odd=0
for i in range(1, number+1):
    num = int(input())
    if i%2==0:
        sum_even+=num
    elif not i%2==0:
        sum_odd+=num

if sum_even==sum_odd:
    print(f"Yes ,sum = {sum_even}")
else:
    diff = abs(sum_even-sum_odd)
    print(f"No, diff = {diff}")
