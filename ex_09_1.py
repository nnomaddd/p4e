fhand = open('romeo.txt')
for line in fhand:
    line = line.rstrip()
    line = line.split()
    
    print(line)