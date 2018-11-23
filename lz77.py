code = []

WINDOW_MAX_SIZE = 5

print('Введите строку для кодирования')
s = input()

window = ''
buffer = ''
occ = -1

i = 0
for char in s:
    i += 1
    if buffer == '':
        if char not in window:
            window = window + char
            code.append((0, 0, char))
        else:
            buffer += char
            occ = window.find(char)
            if i == len(s):
                code.append((len(window) - occ, len(buffer), '<string end>'))
    else:
        buffer += char
        if i == len(s):
            code.append((len(window) - occ, len(buffer), '<string end>'))
        if window[(occ + len(buffer) - 1) % len(window)] == char:
            continue
        else:
            code.append((len(window) - occ, len(buffer) - 1, char))
            window += buffer
            if len(window) > WINDOW_MAX_SIZE:
                window = window[len(window) - WINDOW_MAX_SIZE:len(window)]
            buffer = ''
            occ = -1

print(code)
