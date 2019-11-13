from termcolor import colored

class Some:
    def __init__(self, foo, name='mayday'):
        self.name = name
        self.foo  = foo
        print(colored('=== init ===', 'yellow'))
        print('your foo is {}'.format(self.foo))

    @staticmethod
    def staticMethod(obj, num1):
        print(colored('>>> static method ===', 'yellow'))
        print('your obj is {}, and num1 is {}'.format(obj.foo, num1))
        print("static method ge obj id is {}".format(id(obj)))

    
    @classmethod
    def classMethod(cls, obj, num1):
        print(colored('>>> class method', 'yellow'))
        print('your cls is {}, num1 is {}'.format(cls, num1))
        print(id(cls))

    def sayHello(self):
        print(colored('>>> sayHello func', 'yellow'))
        print(self.name+' says Hello to you!! :D')
        print("your obj id is {}".format(self))




# test1:
s1 = Some('okla', 'osis')
Some.staticMethod(s1, num1=99)
Some.sayHello(s1)


# 宣告另一個instance s2, 並印出s1及s2的記憶體位址 
s2 = Some('well done', 'big bang')
print('s1 id ={}, s2 id ={}'.format(id(s1), id(s2)))


print(colored('== use class to call method', 'green'))
# Some.classMethod(num1=444)     

print(colored('== use instance to call method', 'green'))
s1.classMethod(obj=s1, num1=666)   
s2.classMethod(obj=s2, num1=888)

print(colored('== send the obj to self', 'green'))
Some.sayHello(s1)
Some.sayHello(s2)