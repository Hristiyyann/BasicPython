country = input()
while country != "End":
    budget = float(input())
    new_budget = 0
    while new_budget < budget:
        money = float(input())
        new_budget += money
        if new_budget >= budget:
            print(f"Going to {country}!")
    country = input()
