number = input()
prime_sum = 0
nonprime_sum = 0
flag = 0

while number != 'stop':
    number = int(number)
    flag = 0
    if number < 0:
        print('Number is negative.')
    else:
        for devision_number in range(2, number):
            if number % devision_number == 0:
                flag = 1
                break
        if flag:
            nonprime_sum += number
        else:
            prime_sum += number

    number = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {nonprime_sum}')
