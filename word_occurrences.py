word_counts = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_counts.get(word, 0)
    word_counts[word] = frequency + 1
