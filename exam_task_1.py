bitcoins = int(input())
yuans = float(input())
comission = float(input())

sum = (bitcoins * 1168) + ((yuans * 0.15) * 1.76)
sum /= 1.95
sum *= (1-(comission/100))

print(f"{sum:.2f}")
