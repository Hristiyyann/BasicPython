n1 = int(input())
n2 = int(input())
operation = input()
result = 0
even_or_odd = ''
flag = 0
if operation == '+':
    result = n1 + n2
elif operation == '-':
    result = n1 - n2
elif operation == '*':
    result = n1 * n2
elif operation == '/':
    if n2 == 0:
        flag = 1
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
elif operation == '%':
    if n2 == 0:
        flag = 1
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2

if operation == '+' or operation == '-' or operation == '*':
    if result % 2 == 0:
        even_or_odd = '- even'
    elif result % 2 == 1:
        even_or_odd = '- odd'
if flag == 0 and operation != '/':
    print(f'{n1} {operation} {n2} = {result} {even_or_odd}')
elif flag == 0:
    print(f'{n1} {operation} {n2} = {result:.2f} {even_or_odd}')
