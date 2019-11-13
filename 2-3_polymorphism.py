class Father:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Father: num1 is {}, num2 is {}".format(num1, num2))


    @classmethod
    def clsMethodInt(cls, objNum, num1, num2):
        objList = [cls(num1+i, num2+i) for i in range(objNum)]

        return objList

    def show(self):
        print('num1={}, num2={}'.format(self.num1, self.num2))


fList = Father.clsMethodInt(objNum=5, num1=10, num2=20)

for f in fList:
    f.show()
        
        

