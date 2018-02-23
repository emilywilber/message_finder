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



with open("C:/Users/ewilbe5944/project/snel/text_files/file_012347.txt", 'r') as f:
        readcontent = f.read()
        f.close()

counts = [0] * 127
for c in readcontent:
    n = ord(c)
    counts[n] += 1
counts = counts[32:127]

print(chi_square(counts))

'''
89
94
82
63 las one
102
77 ish 
'''
