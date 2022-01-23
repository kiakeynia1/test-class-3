import random

words = ['book', 'dog', 'kia', 'clock', 'engineer', 'bag']

word = random.choice(words)

horof = len(word)

for n in range(horof):
    print("-", end=" ")

joon = 10

while joon > 0:

    user_Character = input()

    if user_Character in word:
        
        print("yes")
    else:
        joon = joon - 1
        print(joon)


    