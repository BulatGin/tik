code = []

dictionary = {'': 0}

print('Введите строку для кодирования')
s = input()

buffer = ''

for char in s:
    word = buffer + char
    if word in dictionary:
        buffer += char
    else:
        code.append((dictionary[buffer], char))
        dictionary[word] = len(dictionary)
        buffer = ''

print(code)
