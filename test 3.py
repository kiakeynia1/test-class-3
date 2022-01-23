c = []

c.append(1)
c.append(1)

for i in range(2, 20):
    x = c[i-1] + c[i-2]
    c.append(x)


print(c)