def missing_number(seq):
    origianal = [x for x in range(seq[0],seq[-1]+1)]
    seq = set(seq)
    return (list(seq ^ set(origianal)))
print(missing_number([1,2,4,5,6,8,10]))


a = [1,2,4,5,7,9]
res = [ele for ele in range(max(a) +1) if ele not in a]
print(res)


