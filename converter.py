number = float(input())
vh_ed = input()
izh_ed = input()
new = 0

if vh_ed == "m" and izh_ed == "cm":
    new = (number * 100)
elif vh_ed == "m" and izh_ed == "mm":
    new = number * 1000
elif vh_ed == "cm" and izh_ed == "m":
    new = number / 100
elif vh_ed == "cm" and izh_ed == "mm":
    new = number * 10
elif vh_ed == "mm" and izh_ed == "m":
    new = number / 1000
elif vh_ed == "mm" and izh_ed == "cm":
    new = number / 10

print(f'{new:.3f}')

