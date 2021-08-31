x = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(x))
y = []
z = len(x) - 1

while z >= 0:
    y.append(x[z])
    z = z - 1
print(y)