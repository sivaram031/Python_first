

class parent():

    def add(self,a,b):

        print(a + b)

class child(parent):

    def multi(self):
        super().add(self.a ,self.b)
        print(self.a,self.b)

obj = parent()
obj.add(4,5)
print(obj.add)

l = ['a','b']
l2 =[1,2,3]

l3 = dict(zip(l,l2))
print(l3)

file = open('launch_broswer.py','r')
s = file.seek(6)
print(s)