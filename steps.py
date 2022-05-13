steps_to_reach = 10000
total_steps = 0

while total_steps < 10000:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        total_steps += steps
        break

    steps = int(steps)
    total_steps += steps

if total_steps < steps_to_reach:
    print(f'{steps_to_reach - total_steps} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{total_steps - steps_to_reach} steps over the goal!')
