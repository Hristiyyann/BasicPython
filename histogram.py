numbers = int(input())
p1 = p2 = p3 = p4 = p5 = 0
for pos in range(numbers):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif num >= 800:
        p5 += 1

p1 = (p1 / numbers) * 100
p2 = (p2 / numbers) * 100
p3 = (p3 / numbers) * 100
p4 = (p4 / numbers) * 100
p5 = (p5 / numbers) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
