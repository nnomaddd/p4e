def chop(t):
    print('before',t)
    del t[0]
    print('middle',t)
    del t[-1]
    print('after',t)
    return None

def middle(t):
    print('before middle',t)
    return t[1:-1]
    print('after middle',t)
t = [1, 4, 3, 2]
t.sort()
result = chop(t)
print(t)
print(result)
print(middle(t))

