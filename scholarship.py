salary = int(input("Salary = "))
success = float(input("Success = "))
min_salary = int(input("Minimal salary is = "))

flag = 0
if 4.5 <= success < 5.5:
    if salary < min_salary:
        scholarship = min_salary * 0.25
        flag = 1
    else:
        print("You cannot get a scholarship")
elif success >= 5.5:
    scholarship = success * 25
    flag = 1
else:
    print("You cannot get a scholarship")

if flag == 1:
    print(scholarship)
