fname = input("Enter file name: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()
count=0
total=0.0
for line in fhand:
    if line.find("X-DSPAM-Confidence:") == -1: continue
    count += 1
    value = (float(line[19:26]))
    total += value
    if count > 0:
        average = total / count
        x = type(fname)
print(x)
print(average)
print(line)
print(count)
