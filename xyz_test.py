class abc:
    
    def __init__(self):
        self.a = 10
        self.b = 30
        print(self.b)
    def multi(self,n):
        print("this is value of b : "+str(self.b))
        self.n = n
        return (self.n*self.a)
    def add(self):
        self.first = "shyam"
        self.second = "goli"
        print(self.first + self.second)

class prq(abc):
    ob = abc()
    print(ob.b)
    def pr(self):
        print(f"this is first {self.a} and this is second {self.n}")

obj = prq()
obj.multi(20)
obj.add()
obj.pr()


