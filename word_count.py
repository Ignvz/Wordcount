happy =(input("Enter a STATEMENT:"))

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
