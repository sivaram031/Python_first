

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

