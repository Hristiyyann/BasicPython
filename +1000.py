word = input("Word")
length = len(word)
sum = 0
for count in range(length):
    char = word[count]
    if char == 'a':
        sum += 1
    elif char == 'e':
        sum += 2
    elif char == 'i':
        sum += 3
    elif char == 'o':
        sum += 4
    elif char == 'u':
        sum += 5
print(sum)