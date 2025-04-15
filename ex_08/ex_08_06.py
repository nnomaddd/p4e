
numbers = []

while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numbers.append(value)
print('Maximum',max(numbers))
print('Minimum',min(numbers))

