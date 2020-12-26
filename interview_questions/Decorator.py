
def service(fun):
    def inner(*args):
        amt = fun(*args)               # Decorator  implementation
        new_amt = amt + amt * 0.7
        return new_amt
    return inner

@service
def customer(a,b):
    return a+b
final =customer(100,200)
print(final)