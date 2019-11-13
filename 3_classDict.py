class Some:
    wow=1234
    def __init__(self, name):
        self.name=name


print('=== check Class __dict__ ===')
print(Some.__dict__)

print('=== check Class with vars(yourObj) ===')
print(vars(Some))

print('=== declare a class object ===')
s = Some(name='okla')
print(s.__dict__)

print('=== set a property ===')
s.name='hello'
print(s.__dict__)
print(vars(s))

print('=== del a property ===')
del s.name
print(s.__dict__)


