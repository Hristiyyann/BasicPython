deposit = float(input())
months = int(input())
percent = float(input())

on_lihva = deposit * percent / 100
lihva_for_one = on_lihva / 12
total = deposit + (months * lihva_for_one)
print(total)
