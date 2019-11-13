from termcolor import colored

class Some:
    def __init__(self, name):
        self.name=name
        print("{} is ready! id={}".format(name, id(self)))
        

    @staticmethod
    def stcMethod(*args):
        print('Static:{}'.format(args))

    @classmethod
    def clsMethod(*args):
        print('classMethod:{}, id={}'.format(args[0], id(args[0]))) # <-- 因為args是tuple, 若要取得cls, 則需要先取出element


print(colored('=== static method ===', 'yellow'))
s1 = Some('s1')
s1.stcMethod([1,2,3,4])
Some.stcMethod([1,2,3,4])


# 使用class method, 可以發現, 接收的第一個參數是它所依附的原生class~ Some
print(colored('=== class method ===', 'yellow'))
print("class Some id is {}".format(id(Some)))
Some.clsMethod()
s1.clsMethod()