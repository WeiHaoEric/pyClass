class Father:
    def __init__(self, name, ):
        self.name = 'Hunag'
        print("This is Father class")

    def run(self):
        print('father can run fast')

    def __str__(self):
        return 'Father class'


class Son(Father):
    def __init__(self, name):
        super().__init__(name=name)
        print('This is Son class')
        print('your name is {}'.format(self.name))

    def __str__(self):
        return super().__str__()+' pass to Son'


eric = Son(name='HUANG')
print(eric)