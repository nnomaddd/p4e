fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    #line= line.rstrip()
    words = line.split()
    print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[0])

with open('bad_mbox.txt', w) as f:
    f.write('From user@domain.com\n')
    f.write('From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008\n')