from multimethod import multimethod


@multimethod
def add(a: int,b: int):

    return  'this is addtion',a * b

@multimethod
def add(x,y):
    return 'this is multiplecation',x + y

print(add(4,5))
print(add('sivar','ram'))