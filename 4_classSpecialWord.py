class Some:

    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __repr__(self):
        return "call __repr__ !!"

    def __str__(self):
        return "call __str__!!"

    def __eq__(self, that):
        return self.num1==that.num1 and self.num2==that.num2

    


s1 = Some(num1=10 , num2=20 )
s2 = Some(num1=10, num2=20)

print(s1==s2)
print(s1)
b = s1+'oklas'
print(b)