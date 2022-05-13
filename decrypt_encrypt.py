sentence = "i am so happy to see you"
length = len(sentence)

for word in sentence:
    if word == ' ':
        word = 94
    elif word == 'a' or word == 'e' or word == 'o' or word == 'i' or word == 'u':
        word = ord(word) + 2
    else:
        word = ord(word) + 1

    word = chr(word)

    if word != '^':
        print(f"{word}", end=' ')
    else:
        print(" ",end='')



