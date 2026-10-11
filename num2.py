import re


def func(text):
    words = re.findall(r'[a-zA-Z]+', text)
    K = max(len(x) for x in words)
    cho = ''
    for c in text:
        if 'a' <= c <= 'z':
            cho += chr((ord(c)-ord('a') + K) % 26+ ord('a'))
        elif 'A' <= c <= 'Z':
            cho += chr((ord(c)-ord('A') + K) % 26+ord('A'))
        else:
            cho += c
    return K, cho

K, text = func(input('текст: '))
print(f'k={K}')
print('text -', text)