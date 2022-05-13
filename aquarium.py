length = float(input())
width = float(input())
height = float(input())
percent = float(input())
percent /= 100

volume = length * width * height
liters = volume * 0.001
liters *= (1 - percent)
print(liters)
