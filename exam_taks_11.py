days = int(input())
count_days = 0
total_money = 0
money = 0
count_lose = 0
count_win = 0
all_win = 0
all_lose = 0

while count_days != days:
    sport = input()
    if sport == 'Finish':
        if count_win > count_lose:
            total_money += money // 10

        count_lose = 0
        count_win = 0
        money = 0
        count_days += 1

    if sport == 'win':
        total_money += 20
        money += 20
        count_win += 1
        all_win += 1
    elif sport == 'lose':
        count_lose += 1
        all_lose += 1


if all_win > all_lose:
    total_money += (total_money * 0.2)
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
