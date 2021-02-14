from collections import Counter
def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    print(set (ct_a) ^ set (ct_b))


    print(sum(abs(i) for i in ct_a.values()))


number_needed('cde','abc')

import pandas as pd

df = pd.read_sql()

