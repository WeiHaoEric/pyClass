# class A(object):
#     def method1(self):
#         print('A.method1')
        
#     def method2(self):
#         print('A.method2')
        
# class B(A):
#     def method3(self):
#         print('B.method3')
        
# class C(A):
#     def method2(self):
#         print('C.method2')
        
#     def method3(self):
#         print('C.method3')
        
# class D(B, C):
#     def method4(self):
#         print('D.method4')

# d = D()
# d.method4() # 在 D 找到，D.method4
# d.method3() # 以 D->B 順序找到，B.method3
# d.method2() # 以 D->B->C 順序找到，C.method2
# d.method1() # 以 D->B->C->A 順序找到，A.method1

class A:
    def method1(self):
        print("A method1")


class B(A):
    # def method1(self):
    #     print("B method1")
    
    def method2(self):
        print("B method2")


class C(A):
    def method2(self):
        print("C method2")
    
    def method3(self):
        print("C method3")


class D(B,C):
    def method4(self):
        print("D method4")



d = D()
d.method1() # C->B, A.method1  |  A.method1  
d.method2() # C   , C.method2  |  B.method2
d.method3() # C   , C.method3  |  C.method3
d.method4() # D   , D.method4  |  D.method4