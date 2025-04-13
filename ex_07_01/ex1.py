fhand = open('mbox-short.txt')
userinput = input('Enter a file name: ')
for line in fhand:
    line = line.rstrip()
    if line.find(userinput) == -1: continue
    print (float(line[20:25]))
    
    