nomarat = []

while True:
    nomre = float(input())
    if nomre == -1:
        break

    nomarat.append(nomre)

moadel = sum(nomarat) / len(nomarat)

print(moadel)
