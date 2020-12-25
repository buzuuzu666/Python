a = ["pencil", "apple", "table", "carrot"]

if len(a) % 2 == 0:
    i = 0
    while i < len(a):
        el = a[i]
        a[i] = a[i + 1]
        a[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(a) - 1:
        el = a[i]
        a[i] = a[i + 1]
        a[i + 1] = el
        i += 2

print(a)