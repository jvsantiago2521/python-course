class A:
    
    def quem_sou(self):
        print("A")

class B(A):
    pass
    #def quem_sou(self):
    #    print("B")

class C(A):
    
    def quem_sou(self):
        print("C")

class D(B, C):
    
    def quem_sou(self):
        super().quem_sou()
        print("D")

print(D.mro())
d = D()
d.quem_sou()

