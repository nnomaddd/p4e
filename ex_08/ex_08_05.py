file = input('Enter file name: ')
try:
    with open(file) as fhand:
        count = 0   
        for line in fhand:
            line = line.rstrip()
            words = line.split()
            #print('debug:', words)
            if len(words) == 0: continue
            if words[0] != 'From': continue
            if words[0] == 'From':
                count += 1
            print(words[1])
        print('There were',count, 'lines in the file with From as the first word')
except:
    print('File cannot be opened:', file)