pen = int(input())
markers = int(input())
liters = float(input())
discount = int(input())

sum = (pen * 5.80) + (markers * 7.20) + (liters * 1.20)
sum *= (1-(discount/100))

print(f"{sum:.3f}")
