with open('romeo.txt') as fhand:
    all_words = []
    for line in fhand:
        line= line.lower()
        #print(line)
        line = line.rstrip()
        #print('rstrip',line)
        words = line.split()
        all_words.extend(words)
        #print('split',all_words)
    all_words =
    sort = sorted(all_words)
    print(sort)