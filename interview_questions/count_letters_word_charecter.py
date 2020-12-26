file = open('Document_module.py','r+')

words = 0
charecters = 0
lines = 0

for i in file:
    wordslist = i.split('\n')
    words = words + len(wordslist)
    charecters = charecters + len(i)
    lines = lines + 1

print(words)
print(charecters)
print(lines)