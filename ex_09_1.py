with open('romeo.txt') as fhand:
    all_words = []
    for line in fhand:
        line = line.lower()
        line = line.rstrip()
        words = line.split()
        all_words.extend(words)
    all_words.sort()
    print(all_words)

