def missing_number(seq):
    origianal = [x for x in range(seq[0],seq[-1]+1)]
    seq = set(seq)
    return (list(seq ^ set(origianal)))
print(missing_number([1,2,4,5,6,8,10]))