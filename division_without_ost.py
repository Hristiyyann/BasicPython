numbers = int(input())
p2 = p3 = p4 = 0

for count in range(numbers):
    num = int(input())
    if num % 2 == 0:
        p2 += 1
    if num % 3 == 0:
        p3 += 1
    if num % 4 == 0:
        p4 += 1

p2 = (p2 / numbers) * 100
p3 = (p3 / numbers) * 100
p4 = (p4 / numbers) * 100

print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
