st = "aabccbdefeeghj"
out = []
c = 1
prev = ' '
for i in st:
    if i ==prev:
        c+=1
    else:
        prev=i
        if c>1:
            out.append(str(c))
        out.append(i)
        c =1

print(' '.join(out))
