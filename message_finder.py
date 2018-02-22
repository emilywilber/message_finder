with open('file_000010.txt', 'r') as f:
    readcontent = f.read()
    f.close()

counts = [0] * 127
for c in readcontent:
    n = ord(c)
    counts[n] += 1
counts = counts[32:127]

print(counts)
