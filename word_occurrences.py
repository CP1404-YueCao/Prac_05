word_counts = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_counts.get(word, 0)
    word_counts[word] = frequency + 1
words = list(word_counts.keys())
max_len = max((len(word) for word in words))
for word in words:
    print(f"{word} : {word_counts[word]}")