
def creampie(text):
    words = text.lower().split()
    wordstat = {word: words.count(word) for word in words}
    count = len(wordstat)
    for _ in range(5 if count >= 5 else count):
        word = max(wordstat, key = wordstat.get)
        del wordstat[word]
        print(word)


creampie(input())

