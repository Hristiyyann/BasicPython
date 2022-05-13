pages = int(input())
pages_for_hour = int(input())
days = int(input())

hours_on_day = pages / pages_for_hour
hours_on_day /= days
print(hours_on_day)

