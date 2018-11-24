from math import ceil, log2

code = ''
code_bin = ''

# for simplicity of example, we will use only english alphabet for initial dictionary
dictionary = {chr(i): i-ord('a') for i in range(ord('a'), ord('z') + 1)}

code_length = ceil(log2(len(dictionary)))
border = 2**code_length

print('Введите строку для кодирования')
s = input()

buffer = ''

for char in s:
    word = buffer + char
    if word in dictionary:
        buffer = word
    else:
        code += str(dictionary[buffer])
        code_bin += format(dictionary[buffer], 'b').zfill(code_length)
        dict_len = len(dictionary)
        if dict_len == border:
            code_length += 1
            border *= 2
        dictionary[word] = dict_len
        buffer = char
code += str(dictionary[buffer])
code_bin += format(dictionary[buffer], 'b').zfill(code_length)

print(code, code_bin, sep='\n')
