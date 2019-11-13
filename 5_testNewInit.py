class Some:
    def __new__(cls, isClsInstance):
        print('__new__: 比__init__還要早被呼叫')
        if isClsInstance:
            print(isClsInstance)
            return object.__new__(cls)
        else:
            return None

    def __init__(self, isClsInstance):
        print('__init__')
        print(isClsInstance)

print('=== Assign a True obj')
Some(True)

print('=== Assign a False obj')
Some(False)

print('=== test ===')
Some(555)
