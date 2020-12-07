
inp = input('enter file name : ')
l = 'h'
k = 0
with open(inp,'r') as f:
    for lines in f:
        word = lines.split()
        for i in lines:
            for letters in i:
                if letters ==(l):
                    k = k+1

print(k)
