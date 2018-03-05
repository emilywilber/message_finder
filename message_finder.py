# calculate mean
def mean(inputlist):
    total = 0
    for i in inputlist:
        total += i
    total = total / len(inputlist)
    return total

# CHI SQUARE calculation
def chi_square(inputlist):
    expected = mean(inputlist)
    
    X = 0

    for n in inputlist:
        X += ((n - expected)*(n - expected))/expected

    return X

# main program loop, iterate over all files
# format of the filename is  file00000.txt, file00001.txt, … , file17999.txt

       
for nums in range(18000):
    name = "file_%05d" % nums + ".txt"

    #print("Opening: " + name)

    # open a file, read its contents
    #using this format but you gotta write the path: with open(name, 'r') as f:
    with open("/Users/ewilbe5944/project/snel/text_files/" + name, 'r') as f:
        readcontent = f.read()
        f.close()

    # populate counts with number of occurences of each letter
    counts = [0] * 127
    for c in readcontent:
        n = ord(c)
        counts[n] += 1
    # we are only interested in values above 32    
    counts = counts[32:127]

    X2 = chi_square(counts)
    if X2 > 140:
        print(name + " is over 140")
        print("chi chi = %d" % X2)

