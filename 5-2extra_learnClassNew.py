class SOME:
    __instance = None
    def __new__(cls):
        print('[__new__]: new class before init...')
        if not SOME.__instance:
            print('__instance賦予一個新的instance給他, return有東西, 所以會跑init函式')
            SOME.__instance = object.__new__(cls)
            return SOME.__instance
        else:
            print('因為__instance已經存在, return None, 所以不會被跑init函式')
            return None

    def __init__(self):
        print('[init]: init class...')


    def doSomething(self):
        print("nothing's to do ")

print('=== 先宣告一次SOME ===')
a = SOME()


print('=== 再次宣告一次SOME ===')
b = SOME()