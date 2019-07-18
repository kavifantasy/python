class A:
    def m1(self):
        return "m1 method"
    def m2(self):
        return "m2 method"

class B(A,C):
    def m3(self):
        return "m3 method"
    def m4(self):
        return "m4 method"

class C():
    def m5(self):
        return "m5 method"
    def m6(self):
        return "m6 method"
      
a=A()
b=B()
c=C()
print(a.m1())
print(a.m2())
print(b.m1())
print(b.m4())
print(c.m1())
print(b.m5())