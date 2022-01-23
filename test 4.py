from re import I
import time
from termcolor import colored

start = time.time()
Number = 0
for i in range(100000000):
    Number += I

print(colored("finished",  "green"))
print(f"ellapsed time: {time.time() - start} s")

