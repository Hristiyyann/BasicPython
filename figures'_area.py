import math
figure = input()
area = 0

if figure == "rectangle":
    side_length = float(input())
    side_width = float(input())
    area = side_length * side_width
elif figure == "square":
    side = float(input())
    area = side * side
elif figure == "triangle":
    h = float(input())
    side = float(input())
    area = (h * side)/2
elif figure == "circle":
    r = float(input())
    area: float = math.pi * r**2

print(area)
