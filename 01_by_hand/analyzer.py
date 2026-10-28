"""Simple word counter — intentionally beginner-level Python."""

text = input("Enter a sentence: ")
words = text.lower().split()
counts = {}

for word in words:
    word = word.strip(".,!?;:\"'()")
    if word:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print("\nTotal words:", sum(counts.values()))
print("Unique words:", len(counts))
print("\nWord counts:")
for word in sorted(counts):
    print(word, counts[word])
