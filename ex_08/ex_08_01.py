total = 0
count = 0
while True:
    inp = input("Enter a number (or 'done' to finish): ")
    if inp == "done":
        break
    value = float(inp)
    total += value
    count = count + 1

average = total / count
print("Average:", average)