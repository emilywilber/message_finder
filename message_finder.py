for nums in range(0, 100):
    name = "file_%d" % nums + ".txt"
    if len(name) == 14:
        name = "file_0%d" % nums + ".txt"
    if len(name) == 13:
        name = "file_00%d" % nums + ".txt"
    if len(name) == 12:
        name = "file_000%d" % nums + ".txt"
    if len(name) == 11:
        name = "file_0000%d" % nums + ".txt"
    if len(name) == 10:
        name = "file_00000%d" % nums + ".txt"
    
with open("/Users/ewilbe5944/project/snel/text_files/" + name, 'r') as f:
    readcontent = f.read()
    f.close()


def mean(inputlist):
    total = 0
    for i in inputlist:
        total += i
    total = total / len(inputlist)
    return total

def chi_square(inputlist):
    expected = mean(inputlist)
    
    X = 0

    for n in inputlist:
        X += ((n - expected)*(n - expected))/expected

    return X

counts = [0] * 127
for c in readcontent:
    n = ord(c)
    counts[n] += 1
counts = counts[32:127]

if chi_square(counts) > 100:
     print(name)
#ok so it works but it only print the last numbered file
