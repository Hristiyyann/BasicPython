record = float(input())
distance = float(input())
time_for_1_meter = float(input())

whole_time = time_for_1_meter * distance
plus_time = distance // 15
whole_time += plus_time * 12.5

if whole_time < record:
    print(f'Yes, he succeeded! The new world record is {whole_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {whole_time - record:.2f} seconds slower.')
