def func(text):
    text = text.split()
    new_text = ''
    for word in text:
        new_text+=f'{word[::-1]} '
    return (' '.join(text[::-1]), new_text)

text1, text2 = func(input("текст: "))
print('-', text1)
print('-', text2)