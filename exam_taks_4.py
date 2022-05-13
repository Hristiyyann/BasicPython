record = float(input())
dictance = float(input())
seconds = float(input())

total = dictance * seconds
total += (dictance // 50) * 30

if total >= record:
    print(f'No! He was {total - record:.2f} seconds slower.')
else:
    print(f'Yes! The new record is {total:.2f} seconds.')
