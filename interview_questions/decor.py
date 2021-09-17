def serive_tax(fun):
    def inner(*args):
        amt = fun(*args)
        newamount = amt + amt * 0.07
        return newamount
    return inner

@serive_tax
def customre(x,y):
    return x+y

final = customre(100,200)
print(final)
