# class abc:
    
#     def __init__(self):
#         self.a = 10
#         self.b = 30
#         print(self.b)
#     def multi(self,n):
#         print("this is value of b : "+str(self.b))
#         self.n = n
#         return (self.n*self.a)
#     def add(self):
#         self.first = "shyam"
#         self.second = "goli"
#         print(self.first + self.second)

# class prq(abc):
#     ob = abc()
#     print(ob.b)
#     def pr(self):
#         print(f"this is first {self.a} and this is second {self.n}")

# obj = prq()
# obj.multi(20)
# obj.add()
# obj.pr()


# class abc:
#     def f(self,a,b):
#         self.a  = a
#         self.b = b
#     def add(self):
#         return (self.a + self.b)

# obj = abc.(30,20)
# print(obj.add())

# class MyClass:
#     def __init__(self):
#         self.__a = 10

#     def func(self):
#         print("I am in func")

# obj = MyClass() 
# print(obj.__a)

# print(li)


# print(list(map(str,st.split(chr(64+i) for i in range(1,27)))))
# print(list(map(str,st.split("T"))))
# for i in range(1,27):
#     pri
# chr(64+i)
# print()


st = "VikeshTest"
li = list(chr(64+i) for i in range(1,27))
split_posi = []
for i in st:
    if i in li:
        split_posi.append(st.index(i))
print(st[split_posi[0]:split_posi[1]])
print(st[split_posi[1]:])