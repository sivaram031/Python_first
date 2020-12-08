import os

print(os.listdir())
lst = []

for i in os.listdir():
    if i.endswith('.txt'):
        lst.append(i)
        print(i)


